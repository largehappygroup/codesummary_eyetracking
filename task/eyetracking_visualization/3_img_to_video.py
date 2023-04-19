import glob
import moviepy.editor as mpy
import os
import re
from tqdm import tqdm

os.chdir('/home/zachkaras/codeSummary_eyetracking/codesummary_eyetracking/task/eyetracking_visualization/video_frames_out/11_29/')
output_dir = '../../videos/'
fps = 30
file_list = glob.glob('*.jpg')
lsorted = sorted(file_list, key=lambda x: int(os.path.splitext(x)[0]))  
clip = mpy.ImageSequenceClip(lsorted, fps=fps)
clip.write_videofile("../../11_29_full.mp4")