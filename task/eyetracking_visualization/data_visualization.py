import numpy as np
import os
import cv2
import re
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
pid = 168
os.chdir('../data/{pid}/gaze/'.format(pid=str(pid)))
#eye_files = '../data/168/'

#frame_dir = '11_29/'
framelist = os.listdir('.')
stimlist = os.listdir('../../../bounding_boxes/final_stimuli')
# print(framelist)
# print(stimlist)
frame_out_dir = '../../video_frames_out/{pid}/'.format(pid=str(pid))
framelen = len(framelist)
framelist.sort()
stimlist.sort()

try:
    os.mkdir(frame_out_dir)
except:
    pass

counter = 0 
for i in range(framelen):
    #print(type(framelist[i]))
    if re.search("reading", framelist[i]):
        task = "reading"
    elif re.search("writing", framelist[i]):
        task = "writing"
    func = re.search('_[a-zA-Z0-9]*\.csv', framelist[i])
    func = func[0][1:-4]
    print(func)
    # if task is reading, do frankenstein maneuver on screenshot
    #func = re.search()
# TODO - iterate through eye-tracking files (framelist)
# Iterate through each file
# Find the corresponding image (might need to adjust pixels of screenshots)
# For each row, plot gaze coordinates on image
exit(1)
csv_dir = '../../../data/002/gaze/'
csv_file = '002_full_task.csv'

df = pd.read_csv(csv_dir + csv_file)
df.columns = ['participant_id', 'function_name', 'function_id', 'system_timestamp', 'device_timestamp', 
              'valid_gaze_left', 'valid_gaze_right', 'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 
              'valid_pd_right', 'gaze_left', 'gaze_right']
#df.columns = ["pid", "function_name", "function_id", "system_timestamp", "device_timestamp", "valid_gaze_left",
#              "valid_gaze_right", "gaze_left", "gaze_right", "valid_pd_left", "valid_pd_right", "pd_left", "pd_right"]

dflen = len(df)
df_valid = df[(df['valid_gaze_left'] == 1)]
df_valid = df[(df['valid_gaze_right'] == 1)]
df_valid = df[(df['valid_pd_right'] == 1)]
df_valid = df[(df['valid_pd_left'] == 1)]

img_path = os.getcwd() + '/' + framelist[0]
img = cv2.imread(img_path)
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]

starttime = int(df_valid.iloc[0, 3])  # in microseconds
endtime = int(df_valid.iloc[-1, 3])  # in microseconds
duration = endtime-starttime

df_valid['adjusted_timestamp'] = df_valid.apply(lambda row: (
    row['system_timestamp'] - starttime)/(10**6), axis=1)
df['adjusted_timestamp'] = df.apply(lambda row: (
    row['system_timestamp'] - starttime)/(10**6), axis=1)

def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i]-K))]

time_series = df['adjusted_timestamp']
valid_time_series = df_valid['adjusted_timestamp']

# given the gaze vector, return the x/y position for the gaze point in open-cv video
def return_x_y(gaze):
    pattern = "[()]"
    new_gaze_string = re.sub(pattern, "", gaze)
    
    xyz = new_gaze_string.split(',')
    if xyz[0] == 'nan' or xyz[1] == 'nan':
        return "oof", "oof"
    
    x = round(width*float(xyz[0]))
    y = round(height*float(xyz[1]))

    return x, y

for k, j in enumerate(tqdm(framelist)):
    i = int(re.findall("\d+",j)[0]) - 333 # subtract frame numbers here if starting in the middle 
    img_path = os.getcwd() + '/' + framelist[k]
    # time from the video
    t = i/30
    # time in raw data
    t1 = closest(list(time_series), t)
    t_index = list(time_series).index(t1)

    if df.loc[t_index, 'valid_gaze_left'] == 1:
        gaze_l = df.loc[t_index, 'gaze_left']
        gaze_r = df.loc[t_index, 'gaze_right']
        cv_x_l, cv_y_l = return_x_y(gaze_l)
        cv_x_r, cv_y_r = return_x_y(gaze_r)
        
        temp = [cv_x_l, cv_y_l, cv_x_r, cv_y_r]
        if "oof" in temp:
            continue
        
        img = cv2.imread(img_path)
        cv2.circle(img, (cv_x_l, cv_y_l), 10, (0, 255, 0), -1)
        cv2.circle(img, (cv_x_r, cv_y_r), 10, (255, 0, 0), -1)
        cv2.imwrite(frame_out_dir + '/' + re.findall("\d+", j)[0] + '.jpg', img)
    else:
        t_2 = closest(list(valid_time_series), t)

        if abs(t_2 - t) <= 0.1:
            t2_index = valid_time_series[valid_time_series == t_2].index[0]
            gaze_l = df.loc[t_index, 'gaze_left']
            gaze_r = df.loc[t_index, 'gaze_right']

            cv_x_l,cv_y_l = return_x_y(gaze_l)
            cv_x_r,cv_y_r = return_x_y(gaze_r)
            
            temp = [cv_x_l, cv_y_l, cv_x_r, cv_y_r]
            if "oof" in temp:
                continue
            
            img =cv2.imread(img_path)
            cv2.circle(img,(cv_x_l, cv_y_l), 10, (0,255,0),-1)
            cv2.circle(img,(cv_x_r,cv_y_r), 10, (255,0,0),-1)
            cv2.imwrite(frame_out_dir + '/' + re.findall("\d+",j)[0] +'.jpg',img) 

        else:
            img = cv2.imread(img_path)
            cv2.imwrite(frame_out_dir + '/' + re.findall('\d+', j)[0] + '.jpg', img)
    
