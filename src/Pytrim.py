from moviepy.editor import *
import sys
from pathlib import Path

class Pytrim:
    def __init__(self, video: str, start: int, end: int):
        self.video = video
        self.start = start
        self.end = end
        clip = VideoFileClip(video)
        clip = clip.subclip(start, end)
        current_dir = Path().absolute()
        clip.write_videofile(f'{current_dir}/clip_{start}_{end}.mp4')

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Usage: Pytrim.py <filename> <start> <end>")
    if os.path.isfile(sys.argv[1]):
        video = sys.argv[1]
    else:
        print(f'Video file does not exist. Please confirm that you are using {sys.argv[1]}')
    start, end = sys.argv[2], sys.argv[3]
    Pytrim(video, start, end)