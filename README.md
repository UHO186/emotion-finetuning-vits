text cleaner from https://github.com/CjangCjengh/vits

original repo1: https://github.com/jaywalnut310/vits

original repo2: https://github.com/SayaSS/vits-finetuning.git

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
- "utils.py" 파일의 152번 줄에 있는 "model_dir"을 수정하세요.
- pre-trained 모델을 "model_dir"/checkpoints 디렉토리에 넣으세요.

### 만약 "n_speakers"를 사용자 정의하려면, 이 두 개의 사전 학습(pre-trained) 모델로 대체(replace)해주세요.
- [G_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0-p.pth)
- [D_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0-p.pth)

## Create datasets
- 화자 ID는 0에서 803 사이여야 합니다.
- 약 50개의 오디오-텍스트 쌍이면 충분하며, 100~600 에포크(epoch)는 꽤 좋은 성능을 보일 수 있지만, 더 많은 데이터가 더 좋을 수도 있습니다.
- 모든 오디오 파일을 22050Hz, 16비트, 모노 wav 파일로 리샘플링(resample)하세요.
- 오디오 파일의 길이는 1초 이상 10초 이하여야 합니다.
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
