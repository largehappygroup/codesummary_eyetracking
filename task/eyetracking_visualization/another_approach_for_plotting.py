import numpy as np
import os
import cv2
import re
import random
import statistics
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm

def return_x_y(gaze):
    width = 1920
    height = 1080
    pattern = "[()]" # gaze is formatted as a string, so this puts it back into a tuple
    new_gaze_string = re.sub(pattern, "", gaze)
    
    xyz = new_gaze_string.split(',')
    # returning values associated with gaze
    x = round(width*float(xyz[0]))
    y = round(height*float(xyz[1]))

    return x, y

# function to
def plot_points(img_name, file, gaze_folder, outfolder):
    eye_file = pd.read_csv(f"{gaze_folder}{file}")
    try:
        img = cv2.imread(f"intermediate_images/{img_name}")
    except:
        print(f"image {img_name} couldn't be found")
        return

    for i, row in eye_file.iterrows():
        gaze_l = eye_file.loc[i, 'gaze_left_eye'] # coordinate for time point
        gaze_r = eye_file.loc[i, 'gaze_right_eye']
        cv_x_l, cv_y_l = return_x_y(gaze_l)
        cv_x_r, cv_y_r = return_x_y(gaze_r) # actual coordinates
        x, y = (statistics.fmean([float(cv_x_l), float(cv_x_r)]), statistics.fmean([float(cv_y_l), float(cv_y_r)]))
        # plotting circles onto the image where coordinates are
        img = cv2.imread(f"intermediate_images/{img_name}")
        cv2.circle(img, (int(x), int(y)), 10, (0, 255, 0), -1)
        name = re.sub(".png", f"{i}.png", img_name)
        cv2.imwrite(f"{outfolder}{name}", img)

# iterate through each participant's gaze files in code_summ_data folder
datafolder = "/home/zachkaras/code_summ_data"
folderlist = os.listdir(datafolder)
for pid in folderlist:
    print(pid)
    gaze_folder = f"/home/zachkaras/code_summ_data/{pid}/annotated_gaze/"
    outfolder = f"video_frames_out/{pid}/"
    try:
        os.mkdir(outfolder)
    except:
        print("folder already exists")
        continue
    
    gazefiles = os.listdir(gaze_folder)
    randfiles = random.sample(gazefiles, 10)
    for file in randfiles:
        print(file)
        if re.search("test_10_bug", file) or re.search("setCombo_Value", file):
            continue
        img_name = file.split("_")[-1]
        img_name = re.sub(".csv", ".png", img_name)
        plot_points(img_name, file, gaze_folder, outfolder)

