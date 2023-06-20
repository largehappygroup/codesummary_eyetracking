import glob
import moviepy.editor as mpy
import os
import re
from tqdm import tqdm

#folders = os.listdir("video_frames_out")
folders = ['117']
for pid in folders:
    print(pid)
    #if f"{pid}.mp4" in os.listdir("videos"):
    #    continue
    if int(pid) < 300:
        fps = 120
    elif int(pid) >= 300:
        fps = 60
    file_list = glob.glob(f"video_frames_out/{pid}/*.png")
    file_list.sort()
    print(file_list)
    #clip = mpy.ImageSequenceClip(file_list, fps=fps)
    #clip.write_videofile(f"videos/{pid}.mp4")
