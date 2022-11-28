import glob
import moviepy.editor as mpy
import os
import re
from tqdm import tqdm

os.chdir('/home/zachkaras/codeSummary_eyetracking/codesummary_eyetracking/task/eyetracking_visualization/video_frames_out')
output_dir = '../video_out/'
fps = 30

#for sub_dir in tqdm(os.listdir()):
file_list = glob.glob('*.jpg')
    
lsorted = sorted(file_list, key=lambda x: int(os.path.splitext(x)[0]))
    
clip = mpy.ImageSequenceClip(lsorted, fps=fps)

clip.write_videofile("test.mp4")