import numpy as np
import os
import cv2
import re
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm

########################
### Work in Progress ###
########################

pid = 168
#os.chdir('../data/{pid}/gaze/'.format(pid=str(pid)))
#eye_files = '../data/168/'

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

def plot_points(root, eye_file, image_file):
    # print("root", root)
    # print("image_file", image_file)
    image = cv2.imread('../bounding_boxes/final_stimuli/{image_file}'.format(root=root, image_file=image_file))
    eye_file = pd.read_csv('{root}{eye_file}'.format(root=root, eye_file=eye_file), names=['participant_id', 'function_name', 'function_id', 'system_timestamp', 'device_timestamp', 'valid_gaze_left', 'valid_gaze_right', 'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 'valid_pd_right', 'pd_left', 'pd_right'])
    dimensions = image.shape
    # print(eye_file.shape[0])
    # for i in range(eye_file.shape[0]):
    #     pass
    # find image associated with file
    # iterate through eye-tracking file
    # plot points on new image
    # output to folder
    df_valid = eye_file[(eye_file['valid_gaze_left'] == 1)]
    df_valid = eye_file[(eye_file['valid_gaze_right'] == 1)]
    df_valid = eye_file[(eye_file['valid_pd_right'] == 1)]
    df_valid = eye_file[(eye_file['valid_pd_left'] == 1)]

    # height, width, number of channels in image
    height = image.shape[0]
    width = image.shape[1]
    for i in range(df_valid.shape[0]):
        gaze_l = df_valid.loc[i, 'gaze_left_eye']
        gaze_r = df_valid.loc[i, 'gaze_right_eye']
        cv_x_l, cv_y_l = return_x_y(gaze_l)
        cv_x_r, cv_y_r = return_x_y(gaze_r)

        temp = [cv_x_l, cv_y_l, cv_x_r, cv_y_r]
        if "oof" in temp:
            continue

        img = cv2.imread(img_path)
        cv2.circle(img, (cv_x_l, cv_y_l), 10, (0, 255, 0), -1)
        cv2.circle(img, (cv_x_r, cv_y_r), 10, (255, 0, 0), -1)
        cv2.imwrite(frame_out_dir + '/' +
                    re.findall("\d+", i)[0] + '.jpg', image)
           
    return

    for k, j in enumerate(tqdm(filelist)):
            # subtract frame numbers here if starting in the middle
        i = int(re.findall("\d+", j)[0]) - 333
        img_path = os.getcwd() + '/' + filelist[k]
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
            cv2.imwrite(frame_out_dir + '/' +
                        re.findall("\d+", j)[0] + '.jpg', img)
        else:
            t_2 = closest(list(valid_time_series), t)

            if abs(t_2 - t) <= 0.1:
                t2_index = valid_time_series[valid_time_series == t_2].index[0]
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
                cv2.imwrite(frame_out_dir + '/' +
                            re.findall("\d+", j)[0] + '.jpg', img)

            else:
                img = cv2.imread(img_path)
                cv2.imwrite(frame_out_dir + '/' +
                            re.findall('\d+', j)[0] + '.jpg', img)


#frame_dir = '11_29/'
root = '../data/{pid}/gaze/'.format(pid=pid)
filelist = os.listdir(root)
stimlist = os.listdir('../bounding_boxes/final_stimuli')
frame_out_dir = './video_frames_out/{pid}/'.format(pid=str(pid))
filelen = len(filelist)
filelist.sort()
stimlist.sort()

try:
    os.mkdir(frame_out_dir)
except:
    pass

for i in range(filelen):
    #print(type(framelist[i]))
    if re.search("reading", filelist[i]):
        task = "reading"
    elif re.search("writing", filelist[i]):
        task = "writing"
    func = re.search('_[a-zA-Z0-9]*\.csv', filelist[i])
    func = func[0][1:-4]
    png = (func+'.png')
    #img = cv2.imread('../bounding_boxes/final_stimuli/{png}'.format(png=png))
    vid = plot_points(root, filelist[i], png)
    
    
    # img = cv2.imread('../../../bounding_boxes/final_stimuli{func}.png'.format(func=func))
    # plt.imshow(img)
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

img_path = os.getcwd() + '/' + filelist[0]
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

for k, j in enumerate(tqdm(filelist)):
    i = int(re.findall("\d+",j)[0]) - 333 # subtract frame numbers here if starting in the middle 
    img_path = os.getcwd() + '/' + filelist[k]
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
    
