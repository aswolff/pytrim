from moviepy.editor import *
import sys
import os.path

if __name__ == "__main__":
    if len(sys.argv) <= 3:
        print("Usage: Pytim.py <filename> <start> <end>")
    if os.path.isfile(sys.argv[1]):
        video = sys.argv[1]
    else:
        print(f'Video file does not exist. Please confirm that you are using {sys.argv[1]}')
    start, end = sys.argv[2], sys.argv[3]
    clip = VideoFileClip(video)
    max_duration = clip.duration
    clip = clip.subclip(start, end)
    clip.write_videofile('../clips/trimmed_video.mp4')