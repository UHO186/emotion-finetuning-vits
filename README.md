text cleaner from https://github.com/CjangCjengh/vits

original repo1: https://github.com/jaywalnut310/vits

original repo2: https://github.com/SayaSS/vits-finetuning.git

emotion-vits repo: https://github.com/innnky/emotional-vits.git

emotion-embbeding: https://github.com/audeering/w2v2-how-to

# 사용 방법은 다음과 같습니다.
# 使用方法は以下の通りです
(Suggestion) Python == 3.7

이 저장소에서는 일본어 데이터셋만 사용하여 파인튜닝이 가능합니다. 한국어 데이터셋은 사용할 수 없습니다.

このリポジトリでは、日本語のデータセットのみを使用してファインチューニングが可能です。
## 레포지토리를 복제
## レポジトリを複製
```sh
git clone https://github.com/umjuho/emotion-finetuning-vits.git
```
## Install requirements
## 必要な要件をインストール
```sh
pip install -r requirements.txt
```
## 사전 학습된(pre-trained) 모델을 다운로드
## 事前学習済みモデルをダウンロード
- [G_0.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0.pth)
- [D_0.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0.pth)
- "utils.py" 파일의 152번 줄에 있는 "model_dir"을 수정하세요.("utils.py"ファイルの152行目にある "model_dir"を修正してください。)
- pre-trained 모델을 "model_dir"/checkpoints 디렉토리에 넣으세요.(事前学習済みモデルを「model_dir」/「checkpoints」ディレクトリに配置してください。)

### 만약 "n_speakers"를 사용자 정의하려면, 이 두 개의 사전 학습(pre-trained) 모델로 대체(replace)해주세요.
### もし「n_speakers」をカスタマイズしたい場合は、この2つの事前学習済みモデルで置き換えてください。
- [G_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0-p.pth)
- [D_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0-p.pth)

## データセットの作成
- 화자 ID는 0에서 803 사이여야 합니다.(スピーカーIDは0から803の範囲内である必要があります。)
- 약 50개의 오디오-텍스트 쌍이면 충분하며, 100~600 에포크(epoch)는 꽤 좋은 성능을 보일 수 있지만, 더 많은 데이터가 더 좋을 수도 있습니다.(約50個のオーディオ-テキストのペアがあれば十分であり、100〜600エポックはかなり良い性能を示すことができますが、より多くのデータがあればより良い結果が得られるかもしれません。)
- 모든 오디오 파일을 22050Hz, 16비트, 모노 wav 파일로 리샘플링(resample)하세요.(すべてのオーディオファイルを22050Hz、16ビット、モノラルのwavファイルにリサンプリングしてください。)
- 오디오 파일의 길이는 1초 이상 10초 이하여야 합니다.(オーディオファイルの長さは1秒以上10秒以下である必要があります。)
```
path/to/XXX.wav|speaker id|transcript
```
- Example

```
dataset/001.wav|10|こんにちは。
```
자세한 예시는 filelists/miyu_train.txt 및 filelists/miyu_val.txt 파일을 참조하세요.

詳細な例は、"filelists/miyu_train.txt"および"filelists/miyu_val.txt"ファイルを参照してください。

## 전처리
## 前処理
```sh
python preprocess.py --filelists filelists/filelist_train.txt filelists/filelist_val.txt
```
```sh

## 감성 임베딩을 추출하세요. 이렇게 하면 각 wav 파일에 대해 *.emo.npy 파일이 생성됩니다.
## 感情の埋め込みを抽出します。これにより、各wavファイルに対して*.emo.npyファイルが生成されます。
python emotion_extract.py --filelists filelists/filelist_train.txt filelists/filelist_val.txt
```
configs/config.json" 파일의 "training_files" 및 "validation_files"을 수정하세요.

"configs/config.json"ファイルの「training_files」と「validation_files」を編集してください。

## 학습
## 学習
```sh
# One speakers
python train.py -c configs/config.json -m checkpoints

# Mutiple speakers
python train_ms.py -c configs/config.json -m checkpoints
```
