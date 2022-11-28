# need time from start of video
import numpy as np
import os
import cv2
import re
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
os.chdir('./test/')

frame_dir = '11_27_test/'
framelist = os.listdir('.')
#frame_out_dir = os.path.join('video_frames_out')
frame_out_dir = '../video_frames_out'

try:
    os.mkdir(frame_out_dir)
except:
    pass

framelen = len(framelist)


# read raw data
csv_dir = '../data/001/gaze/'
csv_file = '001.csv'
df = pd.read_csv(csv_dir + csv_file)

df_valid = df[df['FIXME'] == True] # FIXME - column names
# length of raw data
dflen = len(df)

img_path = os.getcwd() + '/video_frames/' + frame_dir + '/' + framelist[0]
img = cv2.imread(img_path)
dimensions = img.shape
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

time_series = df['AdjustedTime'] # FIXME - column names and deltas
valid_time_series = df_valid['AdjustedTime'] # FIXME - same as above

# given the gaze vector, return the x/y position for the gaze point in open-cv video
def return_x_y(gaze):
    pattern = "[()]"
    new_gaze_string = re.sub(pattern, "", gaze) # FIXME - idk what gaze is here
    xyz = new_gaze_string.split(',')
    x = width/2*float(xyz[0])
    y = height/2*float(xyz[1])
    cv_x = round(width/2 + x)
    cv_y = round(height/2 - y)
    return cv_x, cv_y


for j in tqdm(framelist):
    i = int(re.findall("\d+",j[0]))
    img_path = os.getcwd() + '/video_frames/' + frame_dir + '/' + j
    # time from the video
    t = i/30
    # time in raw data
    t1 = closest(list)

    if df['CombinedGazeRayWorldValid'][t_index] == True: # FIXME - same thing
        gaze_l = df['LeftGazeDirection'][t_inex]
        gaze_r = df['RightGazeDirection'][t_index]

        gaze_origin_l = df['LeftGazeOrigin'][t_index]
        gaze_origin_r = df['RightGazeOrigin'][t_index]

        cv_x_l, cv_x_l = return_x_y(gaze_l)
        cv_x_r, cv_x_r = return_x_y(gaze_r)

        img = cv2.cv2.imread(img_path)
        cv2.circle(img, (cv_x_l, cv_y_l), 20, (0, 255, 0), -1)
        cv2.circle(img, (cv_x_r, cv_y_r), 20, (255, 0, 0), -1)
        cv2.imwrite(frame_out_dir + '/' + re.findall("\d+", j)[0] + '.jpg', img)
    else:
        t_2 = closest(list(valid_time_series), t)

        

        if abs(t_2 - t) <= 0.1:
            t2_index = valid_time_series[valid_time_series == t_2].index[0]
            gaze_l = df['LeftGazeDirection'][t2_index]
            gaze_r = df['RightGazeDirection'][t2_index]

            cv_x_l,cv_y_l = return_x_y(gaze_l)
            cv_x_r,cv_y_r = return_x_y(gaze_r)
            
            img =cv2.imread(img_path)
            cv2.circle(img,(cv_x_l, cv_y_l), 20, (0,255,0),-1)
            cv2.circle(img,(cv_x_r,cv_y_r), 20, (255,0,0),-1)
            cv2.imwrite(frame_out_dir + '/' + re.findall("\d+",j)[0] +'.jpg',img) 

        else:
            img = cv2.imread(img_path)
            cv2.imwrite(frame_out_dir + '/' + re.finall('\d+', j)[0] + '.jpg', img)








