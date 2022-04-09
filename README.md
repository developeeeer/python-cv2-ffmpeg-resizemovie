# 動画のリサイズをcv2 ffmpegを使って実装してみた<hr>

## 実行方法
1. ffmpegをバイナリインストールしてApplications/に配置する
   (これに関しては別にどこでも良い)
2. 環境変数に設定しておく必要があるので以下のようにして
   (python-loadenvなどを使用しても良い)
```commandline
~/.zshrc

export IMAGEIO_FFMPEG_EXE="/Applications/ffmpeg"
```
3. pip より各種ライブラリのインストール
```commandline
pip install -r requirements.txt
```
4. files/ フォルダへリサイズしたい動画を保存しておく
5. resize.py のFILE_LISTに対象のファイルパスを入力する
   (ここ手動なのはよくない・・・)
```commandline
FILE_LIST = [
    'files/v0001.mp4',
    'files/v0002.mp4',
    'files/v0003.mp4',
    'files/v0004.mov',
    'files/v0005.mov',
    'files/v0006.mov',
    'files/v0007.mov',
    'files/v0008.mp4',
    'files/v0009.mp4',
]
```
6. python main.pyで実行
   > resize or resizes : [resizeかresizesどちらかを指定]  
   > filename : files/[filenameを拡張子付きで指定]  
   > filenames(xxxw,yyy) : [リサイズしたいファイルパスをカンマ区切りで入力]  
   > is_audio [Y/n] : [y/nどちらかを指定]  
   
   ※各入力未入力時も対応しているのでコードを読んでくだせえ
7. 以上で動くはず

## 最後に
なんか音声がスローになったり、、、サイズがなんか大きくなったり。
コーデックとかエンコードとか色々理解が浅いので、、、
備忘として残しておきます。