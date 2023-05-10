# 원본 레포지토리
# 元のリポジトリー

text cleaner from https://github.com/CjangCjengh/vits

original repo1: https://github.com/jaywalnut310/vits

original repo2: https://github.com/SayaSS/vits-finetuning.git

emotion-vits repo: https://github.com/innnky/emotional-vits.git

emotion-embbeding: https://github.com/audeering/w2v2-how-to

# 먼저 데이터 라벨링을 합니다.
# データラベリングを最初に行います。
- <https://colab.research.google.com/drive/1Ty9rC72OJ0NF4eb4cVg0VUl-_xGGf8rz?usp=sharing>
- <https://coconala.com/> 에서 데이터 라벨링해줄 인력을 찾는 것도 하나의 방법입니다.
---
- https://coconala.com/ でデータのラベリングを手助けしてくれるスタッフを探すことも一つの方法です。
---

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
- "utils.py" 파일의 152번 줄에 있는 "model_dir"을 수정하세요.
- pre-trained 모델을 "model_dir"/checkpoints 디렉토리에 넣으세요.
---
- [G_0.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0.pth)
- [D_0.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0.pth)
- "utils.py"ファイルの152行目にある "model_dir"を修正してください。
- 事前学習済みモデルを「model_dir」/「checkpoints」ディレクトリに配置してください。
---

### 만약 "n_speakers"를 사용자 정의하려면, 이 두 개의 사전 학습(pre-trained) 모델로 대체(replace)해주세요.
### もし「n_speakers」をカスタマイズしたい場合は、この2つの事前学習済みモデルで置き換えてください。
- [G_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/G_0-p.pth)
- [D_0-p.pth](https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/resolve/main/model/D_0-p.pth)

## 데이터셋 생성
## データセットの作成
- 화자 ID는 0에서 803 사이여야 합니다.
- 약 50개의 오디오-텍스트 쌍이면 충분하며, 100~600 에포크(epoch)는 꽤 좋은 성능을 보일 수 있지만, 더 많은 데이터가 더 좋을 수도 있습니다.
- 모든 오디오 파일을 22050Hz, 16비트, 모노 wav 파일로 리샘플링(resample)하세요.
- 오디오 파일의 길이는 1초 이상 10초 이하여야 합니다.
---
- スピーカーIDは0から803の範囲内である必要があります。
- 約50個のオーディオ-テキストのペアがあれば十分であり、100〜600エポックはかなり良い性能を示すことができますが、より多くのデータがあればより良い結果が得られるかもしれません。
- すべてのオーディオファイルを22050Hz、16ビット、モノラルのwavファイルにリサンプリングしてください。
- オーディオファイルの長さは1秒以上10秒以下である必要があります。
---
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

## Gradio 실행
## Gradioを実行します。
```sh
# emotion_embbeding으로 산출한 npy파일을 넣습니다.
# emotion_embeddingで生成されたnpyファイルを入力します。
python3 webui.py -m ex.pth -c ex.json -e ex.npy
```

# Runpod 환경설정
# Runpodの環境設定

## Terminal
```sh
# 순서대로 실행해주세요.
# 以下の順序で実行してください。

apt-get update
apt-get install -y build-essential libssl-dev libffi-dev python3-dev
wget https://cmake.org/files/v3.21/cmake-3.21.0.tar.gz
tar xf cmake-3.21.0.tar.gz
cd cmake-3.21.0
./bootstrap
make -j4
make install
apt-get install unzip
pip install pyopenjtalk
pip install transformers
pip install librosa==0.8.0
pip3 install torch==1.13.1 torchvision torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

## Notebook

1. ```sh
   !git clone https://github.com/UHO186/emotion-finetuning-vits.git
   ```
2. ```sh
   %cd emotion-finetuning-vits
   ```
   - 실행하기 전에 Terminal명령어를 순서대로 실행해주세요. 아니면 빌드할 때 Cmake에러가 발생합니다.
   - 実行する前に、ターミナルコマンドを順番に実行してください。そうしないと、ビルド時にCMakeエラーが発生する可能性があります。
3. ```sh
   !pip install -r requirements.txt
   ```
4. ```sh
   !python preprocess.py --filelists filelists/filelist_train.txt filelists/filelist_val.txt
   ```
5. ```sh
   !python emotion_extract.py --filelists filelists/train.txt filelists/val.txt 
   ```
   ```sh
   # 이 때 rootpath를 wav파일이 저장되어있는 폴더로 지정해주세요.
   # この場合、rootpathをwavファイルが保存されているフォルダに指定してください。
   rootpath = "dataset/nene"
   ```
6. ```sh
   # One speakers
   python train.py -c configs/config.json -m checkpoints

   # Mutiple speakers
   python train_ms.py -c configs/config.json -m checkpoints
   ```
   ```sh
   # config파일의 경로를 지정합니다.
   # configファイルのパスを指定します。
   config/000.json
   ```

# LOSS 그래프 확인
# 損失（LOSS）グラフを確認します。

- 학습을 진행하면 events.out.tfevent~~~ 와 같은 파일이 생성됩니다.
- tensorboard --logdir <folder> --port 6006 그걸 folder에 경로를 지정합니다.
---
- 学習を進めると、events.out.tfevent~~~というファイルが生成されます。
- tensorboard --logdir <folder> --port 6006 folderに指定されたパスで実行します。

# 데이터셋의 기본이 되는 성우 구하기
# データセットの基になる声優を見つける
   
- https://iikoe.org/ or https://coconala.com/ or https://yuruboi.com/ 에서 성우를 구할 수 있습니다.
- https://iikoe.org/ や https://coconala.com/、https://yuruboi.com/ などのウェブサイトで声優を探すことができます。






