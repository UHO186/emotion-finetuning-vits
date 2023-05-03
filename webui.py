# coding=utf-8
import argparse
import utils
import commons
import torch
import sys
import utils
import argparse
import gradio as gr
import webbrowser
from models import SynthesizerTrn
from text import text_to_sequence
from torch import no_grad, LongTensor
import logging
logging.getLogger('numba').setLevel(logging.WARNING)
logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument('--arg1', type=str, default='configs/vtubers.json', help='path to json file')
parser.add_argument('--arg2', type=str, default='nene_final.pth', help='path to checkpoint')
parser.add_argument('--arg3', type=str, default='all_emotions.npy', help='path to emotion file')
args = parser.parse_args()

json_file = args.arg1
checkpoint = args.arg2
emotion_file = args.arg3


def get_text(text, hps):
    text_norm= text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm

hps = utils.get_hparams_from_file(json_file)
net_g = SynthesizerTrn(
    len(symbols),
    hps.data.filter_length // 2 + 1,
    hps.train.segment_size // hps.data.hop_length,
    n_speakers=hps.data.n_speakers,
    **hps.model)
_ = net_g.eval()

_ = utils.load_checkpoint(checkpoint, net_g, None)
all_emotions = np.load(emotion_file)

def create_tts_fn(net_g_ms):
    def tts_fn(text, noise_scale, noise_scale_w, length_scale, emotion_id, speaker_id):
        text = text.replace('\n', ' ').replace('\r', '').replace(" ", "")
        stn_tst= get_text(text, hps_ms)
        with no_grad():
            x_tst = stn_tst.unsqueeze(0).to(device)
            x_tst_lengths = LongTensor([stn_tst.size(0)]).to(device)
            sid = LongTensor([speaker_id]).to(device)
            emotion = emotion_dict[list(emotion_dict.keys())[emotion_id]]
            audio = net_g_ms.infer(x_tst, x_tst_lengths, sid=sid, noise_scale=noise_scale, noise_scale_w=noise_scale_w,
                                   length_scale=length_scale, emotion=emotion)[0][0, 0].data.cpu().float().numpy()
        return "Success", (22050, audio)
    return tts_fn

download_audio_js = """
() =>{{
    let root = document.querySelector("body > gradio-app");
    if (root.shadowRoot != null)
        root = root.shadowRoot;
    let audio = root.querySelector("#tts-audio").querySelector("audio");
    let text = root.querySelector("#input-text").querySelector("textarea");
    if (audio == undefined)
        return;
    text = text.value;
    if (text == undefined)
        text = Math.floor(Math.random()*100000000);
    audio = audio.src;
    let oA = document.createElement("a");
    oA.download = text.substr(0, 20)+'.wav';
    oA.href = audio;
    document.body.appendChild(oA);
    oA.click();
    oA.remove();
}}
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--api', action="store_true", default=False)
    parser.add_argument("--share", action="store_true", default=False, help="share gradio app")
    parser.add_argument("--colab", action="store_true", default=False)
    parser.add_argument('-c', '--config', type=str, default="configs/config.json", help='JSON file for configuration')
    parser.add_argument('-m', '--model', type=str, required=True,  help='Model path')
    args = parser.parse_args()
    device = torch.device(args.device)
    hps_ms = utils.get_hparams_from_file(args.config)
    models = []
    net_g_ms = SynthesizerTrn(
        len(hps_ms.symbols),
        hps_ms.data.filter_length // 2 + 1,
        hps_ms.train.segment_size // hps_ms.data.hop_length,
        n_speakers=hps_ms.data.n_speakers,
        **hps_ms.model)
    utils.load_checkpoint(args.model, net_g_ms, None)
    _ = net_g_ms.eval().to(device)
    models.append((net_g_ms, create_tts_fn(net_g_ms,)))
    with gr.Interface(
            fn=tts_fn,
            inputs=[gr.inputs.Textbox(label="Text", lines=5, value="今日はいい天気ですね。"),
                    gr.inputs.Slider(label="noise_scale", minimum=0.1, maximum=1.0, step=0.1, value=0.6),
                    gr.inputs.Slider(label="noise_scale_w", minimum=0.1, maximum=1.0, step=0.1, value=0.668),
                    gr.inputs.Slider(label="length_scale", minimum=0.1, maximum=2.0, step=0.1, value=1.0),
                    gr.inputs.Number(label="speaker_id", value=10)],
            outputs=[gr.outputs.Textbox(label="Output Message"), gr.outputs.Audio(label="Output Audio")],
            allow_flagging=False,
            layout="vertical",
            title="TTS Synthesizer",
            description="This is a TTS Synthesizer based on TransformerTTS."
    ) as iface:
        if args.colab:
            iface.launch(inline=False)
        elif args.api:
            iface.launch(share=True)
        else:
            iface.launch()

    with gr.Interface(
            fn=tts_fn,
            inputs=[gr.inputs.Textbox(label="Text", lines=5, value="今日はいい天気ですね。"),
                    gr.inputs.Slider(label="noise_scale", minimum=0.1, maximum=1.0, step=0.1, value=0.6),
                    gr.inputs.Slider(label="noise_scale_w", minimum=0.1, maximum=1.0, step=0.1, value=0.668),
                    gr.inputs.Slider(label="length_scale", minimum=0.1, maximum=2.0, step=0.1, value=1.0),
                    gr.inputs.Number(label="Emotion ID", min_value=0, max_value=len(emotion_dict)-1, step=1, value=0),
                    gr.inputs.Number(label="speaker_id", value=10)], 
            outputs=[gr.outputs.Textbox(label="Output Message"), gr.outputs.Audio(label="Output Audio")],
            allow_flagging=False,
            layout="vertical",
            title="TTS Synthesizer",
            description="This is a TTS Synthesizer based on TransformerTTS."
    ) as iface:
        if args.api:
            if args.share:
                iface.share()
            else:
                iface.launch()
        elif args.colab:
            iface.launch(inline=False)
        else:
            iface.launch()
                   

