import cv2
import moviepy.editor as mp
from moviepy.config import change_settings

change_settings({"FFMPEG_BINARY": "/Applications/ffmpeg"})

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
FPS = 28
MIN_SIZE = 500


def set_audio(old_video, new_video, cut_voice, new_movie_voice):
    try:
        clip_in = mp.VideoFileClip(old_video).subclip()
        clip_in.audio.write_audiofile(cut_voice)
        clip_out = mp.VideoFileClip(new_video).subclip()
        clip_out.write_videofile(new_movie_voice, audio=cut_voice)
    except Exception as e:
        print(e)
        print(f"ERR: 音声のセットに失敗しました[{old_video}]")


def resize_width_height(width, height) -> (int, int):
    if width > height:
        if height < MIN_SIZE:
            return width, height
        else:
            res_height = MIN_SIZE
            res_width = int((MIN_SIZE / height) * width)
            return res_width, res_height
    else:
        if width < MIN_SIZE:
            return width, height
        else:
            res_width = MIN_SIZE
            res_height = int((MIN_SIZE / width) * height)
            return res_width, res_height


def resize(file_path=None, is_audio=True):
    if file_path is None:
        file_path = FILE_LIST[0]
    video_capture = cv2.VideoCapture(file_path)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print(f"OLD: width:{width}, height:{height}, fps:{fps}")

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    new_width, new_height = resize_width_height(width, height)
    filename = f'{file_path.split("/")[-1].split(".")[0]}_resize.mp4'
    print(f"NEW: width:{new_width}, height:{new_height}, fps:{FPS}")
    writer = cv2.VideoWriter(filename, fourcc, FPS, (new_width, new_height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        frame = cv2.resize(frame, (new_width, new_height))
        writer.write(frame)

    video_capture.release()
    writer.release()
    cv2.destroyAllWindows()

    if is_audio:
        set_audio(
            file_path,
            filename,
            f'{file_path.split("/")[-1].split(".")[0]}_audio.mp3',
            f'{filename.split(".")[0]}_audio.mp4'
        )


def resizes(file_path_list=None, is_audio=True):
    if file_path_list is None:
        file_path_list = FILE_LIST
    for file_path in file_path_list:
        resize(file_path, is_audio)
