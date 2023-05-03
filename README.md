text cleaner from https://github.com/CjangCjengh/vits

original repo: https://github.com/jaywalnut310/vits
original repo: https://github.com/SayaSS/vits-finetuning.git

emotion-vits repo: https://github.com/innnky/emotional-vits.git

## Online training and inference
### colab
See [vits-finetuning](https://colab.research.google.com/drive/13FF2pBWxj9rMR1SjI_JpVD6mTRN-kq--?usp=share_link)

# How to use
(Suggestion) Python == 3.7

이 저장소에서는 일본어 데이터셋만 사용하여 파인튜닝이 가능합니다. 한국어 데이터셋은 사용할 수 없습니다.
## Clone this repository
```sh
git clone https://github.com/umjuho/emotion-finetuning-vits.git
```
## Install requirements
```sh
pip install -r requirements.txt
```
## Download pre-trained model
- [G_0.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0.pth)
- [D_0.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0.pth)
- Edit "model_dir"(line 152) in utils.py
- Put pre-trained models in the "model_dir"/checkpoints

### 만약 "n_speakers"를 사용자 정의하려면, 이 두 개의 사전 학습(pre-trained) 모델로 대체(replace)해주세요.
- [G_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0-p.pth)
- [D_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0-p.pth)

## Create datasets
- Speaker ID should be between 0-803.
- About 50 audio-text pairs will suffice and 100-600 epochs could have quite good performance, but more data may be better. 
- Resample all audio to 22050Hz, 16-bit, mono wav files.
- Audio files should be >=1s and <=10s.
```
path/to/XXX.wav|speaker id|transcript
```
- Example

```
dataset/001.wav|10|こんにちは。
```
For complete examples, please see filelists/miyu_train.txt and filelists/miyu_val.txt.

## 전처리
```sh
python preprocess.py --filelists filelists/filelist_train.txt filelists/filelist_val.txt
```
```sh
python emotion_extract.py --filelists filelists/filelist_train.txt filelists/filelist_val.txt
```
Edit "training_files" and "validation_files" in configs/config.json

## 학습
```sh
# One speakers
python train.py -c configs/config.json -m checkpoints

# Mutiple speakers
python train_ms.py -c configs/config.json -m checkpoints
```
