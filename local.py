import argparse
import utils
import commons
import torch
from models import SynthesizerTrn
from text import text_to_sequence
from torch import no_grad, LongTensor
import logging
import numpy as np
import sounddevice as sd
import queue
import openai
import speech_recognition as sr

logging.getLogger("numba").setLevel(logging.WARNING)
logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("asyncio").setLevel(logging.WARNING)

openai.api_key = ""  # 앞서 생성한 API 키를 입력하세요

parser = argparse.ArgumentParser()
parser.add_argument("--device", type=str, default="cpu")
parser.add_argument(
    "-c",
    "--config",
    type=str,
    default="configs/config.json",
    help="JSON file for configuration",
)
parser.add_argument("-m", "--model", type=str, required=True, help="Model path")
parser.add_argument(
    "-e",
    "--emotion",
    type=str,
    default="all_emotions.npy",
    required=True,
    help="Model path",
)
args = parser.parse_args()


def get_text(text, hps):
    text_norm = text_to_sequence(text, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm


def create_tts_fn(net_g_ms):
    def tts_fn(text, noise_scale, noise_scale_w, length_scale, speaker_id, emotion_id):
        all_emotions = np.load(args.emotion)
        emotion_id = int(emotion_id)
        text = text.replace("\n", " ").replace("\r", "").replace(" ", "")
        stn_tst = get_text(text, hps_ms)
        with no_grad():
            x_tst = stn_tst.unsqueeze(0).to(device)
            x_tst_lengths = LongTensor([stn_tst.size(0)]).to(device)
            sid = LongTensor([speaker_id]).to(device)
            emo = torch.FloatTensor(all_emotions[emotion_id]).unsqueeze(0)
            audio = (
                net_g_ms.infer(
                    x_tst,
                    x_tst_lengths,
                    sid=sid,
                    noise_scale=noise_scale,
                    noise_scale_w=noise_scale_w,
                    length_scale=length_scale,
                    emo=emo,
                )[0][0, 0]
                .data.cpu()
                .float()
                .numpy()
            )
        return audio

    return tts_fn


# 마이크로폰에서 음성 입력 받기
def listen_microphone():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    return audio


# 음성을 텍스트로 변환
def transcribe_audio(audio):
    try:
        text = r.recognize_google(audio, language="en-US")
        return text
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"음성 변환에 에러가 발생했습니다: {e}")


# 실시간 음성을 텍스트로 변환
def real_time_transcription():
    while True:
        audio = listen_microphone()
        text = transcribe_audio(audio)
        if text:
            return text

        # 종료 조건을 설정하고 싶다면 여기에 추가하세요
        # 예: if text == "종료": break


# 음성 재생
def play_audio(audio, sample_rate):
    sd.play(audio, sample_rate)
    sd.wait()


if __name__ == "__main__":
    r = sr.Recognizer()

    real_time_text = real_time_transcription()

    response = openai.Completion.create(
        engine="text-davinci-003",  # 사용할 엔진을 선택하세요 (예: text-davinci-003)
        prompt=real_time_text,
        max_tokens=50,
    )
    answer = response.choices[0].text.strip()
    device = torch.device(args.device)
    hps_ms = utils.get_hparams_from_file(args.config)
    net_g_ms = SynthesizerTrn(
        len(hps_ms.symbols),
        hps_ms.data.filter_length // 2 + 1,
        hps_ms.train.segment_size // hps_ms.data.hop_length,
        n_speakers=hps_ms.data.n_speakers,
        **hps_ms.model,
    )
    utils.load_checkpoint(args.model, net_g_ms, None)
    _ = net_g_ms.eval().to(device)
    tts_fn = create_tts_fn(net_g_ms)

    # 음성 재생에 사용할 샘플 속도
    sample_rate = 22050

    # 음성 재생을 위한 청크 크기 설정
    chunk_size = 1024

    # 음성 재생을 위한 콜백 함수
    def audio_callback(outdata, frames, time, status):
        if status.output_underflow:
            print("Output underflow: increase buffer size in sounddevice settings")
        outdata[:frames] = audio_queue.get()

    # 실시간 음성 재생을 위한 큐
    audio_queue = queue.Queue()

    def generate_audio(text):
        audio = tts_fn(
            text,
            noise_scale=0.6,
            noise_scale_w=0.668,
            length_scale=1.0,
            speaker_id=10,
            emotion_id=10,
        )
        audio_queue.put(audio)

    with sd.OutputStream(
        samplerate=sample_rate,
        channels=1,
        callback=audio_callback,
        blocksize=chunk_size,
    ):
        print("Real-time speech synthesis started. Press Ctrl+C to exit.")
        while True:
            text = answer
            if text == "q":
                break

            generate_audio(text)
