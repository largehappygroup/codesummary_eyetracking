import re
import os
import csv
import numpy as np
import pandas as pd
from statistics import mean

def downsample(df): # data in other location was collected at 60Hz, so downsampling the other data
    downsampled_df = df[::2]
    downsampled_df = downsampled_df.reset_index(drop=True)
    return downsampled_df

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath, low_memory=False) # if pid < 300, downsample
    if df['participant_id'][0] and df['participant_id'][0] < 300:
        df = downsample(df)
    df["Row duration"] = df["system_timestamp"] / 1000000
    return df

def init_variables(filepath, df):
    if re.search("reading", filepath):
        aoi_start = df.columns.get_loc('prewritten')
    elif re.search("writing", filepath):
        aoi_start = df.columns.get_loc('code')
        
    bb_start = df.columns.get_loc("geometry") # start of bounding boxes (bb_start) in dataframe 
    bbs = df.columns[bb_start+1:aoi_start]
    bb_zeros = [0] * len(bbs)
    bb_dict = dict(zip(bbs, bb_zeros))
    bb_dur_dict = {col: [] for col in bbs}
    
    aois = df.columns[aoi_start:-1]
    aoi_zeros = [0] * len(aois)
    aoi_dict = dict(zip(aois, aoi_zeros))
    aoi_dur_dict = {col: [] for col in aois}
    
    return [bb_start, bb_dict, bb_dur_dict, aoi_start, aoi_dict, aoi_dur_dict]

def process_df(start, end, df, fc_dict, dur_dict):
    prev_aoi, curr_aoi, fix_flag, aoi_flag, time = '', '', 0, 0, 0
    for i in range(len(df)):
        idx = np.where(df.iloc[i, start:end] == 1)
        curr_aoi = df.columns[idx[0] + (start)]
        if(idx[0].size > 0):
            curr_aoi = df.columns[idx[0] + (start)]
        else: # if an aoi wasn't hit
            if(fix_flag and aoi_flag): # if the participant was previously fixating and looking at an aoi, increment dictionary
                fc_dict[prev_aoi] += 1
                dur_dict[prev_aoi].append(time)
            time = 0
            fix_flag = 0 # reset variables since participant is no longer looking at an aoi
            aoi_flag = 0
            continue

        if(df["fixation"][i] != 'Fixation' and fix_flag == 1): # they were fixating, but now they're not
            if aoi_flag and curr_aoi[0] == prev_aoi: # if they were focused on an aoi, and it was the same one as before...)
                fc_dict[prev_aoi] += 1
                dur_dict[prev_aoi].append(time)
                time = 0
                fix_flag = 0
                aoi_flag = 0
                continue

            elif not aoi_flag or (curr_aoi[0] != prev_aoi): # otherwise if they're not fixating anymore and they weren't focused on an aoi
                fix_flag = 0 # don't incrememnt dictionary and reset fixation flag. AOI flag is still 0

        elif(df["fixation"][i] != 'Fixation' and fix_flag == 0): # they weren't fixating, and they're still not fixating
            aoi_flag = 0
            time = 0

        elif(df["fixation"][i] == 'Fixation' and fix_flag == 1): # the participant is fixating and they were fixating before
            if aoi_flag and prev_aoi == curr_aoi[0]: # if they're still looking at the same aoi
                diff = df["Row duration"][i] - df["Row duration"][i-1] # finding the duration for this particular row 
                time += diff # incrementing fixation duration by this time difference

            elif aoi_flag and prev_aoi != curr_aoi[0]: # they were focused on the same aoi, but now they're looking at a different aoi
                fc_dict[prev_aoi] += 1
                dur_dict[prev_aoi].append(time)
                time = 0
                aoi_flag = 0
                prev_aoi = curr_aoi[0] # prev aoi will now be current aoi

            elif not aoi_flag and prev_aoi == curr_aoi[0]: # they weren't fixating on the same aoi but now they are
                aoi_flag = 1

            elif not aoi_flag and prev_aoi != curr_aoi[0]:
                prev_aoi = curr_aoi[0] # resetting previous aoi to be current aoi

        elif (df["fixation"][i] == 'Fixation' and fix_flag == 0): # they're fixating, but they weren't before
            fix_flag = 1
            prev_aoi = curr_aoi[0]
            diff = df["Row duration"][i] - df["Row duration"][i-1]
            time += diff

    return fc_dict, dur_dict

def calculate_mean_fixation(dur_dict):
    for key in dur_dict.keys():
        if dur_dict[key]:
            average_dur = mean(dur_dict[key])
        else:
            average_dur = 0
        dur_dict[key] = average_dur

    return dur_dict

def calculate_ratio(fix_dict, dur_dict):
    fc_sum = {}
    for aoi in fix_dict:
        if fix_dict[aoi] > 0: 
            fc_sum[aoi] = fc_sum.get(aoi, 0) + fix_dict[aoi]
    
    for aoi in dur_dict:
        if dur_dict[aoi]: 
            fd_sum = sum(dur_dict[aoi]) 
            fc = fix_dict[aoi] 
            ratio = fd_sum/fc 
            print(f"{aoi} - {ratio}")

def main(): 
    superpath = "/home/zachkaras/code_summ_data"
    participants = os.listdir(superpath)
    for p in participants:
        print(p)
        files = os.listdir(f"{superpath}/{p}/annotated_gaze")
        for file in files:
            print(file)
            filepath = f'{superpath}/{p}/annotated_gaze/{file}'
            df = load_and_preprocess_data(filepath)
            name = filepath.split("_")[-1]
            name = re.sub(".csv", "", name)
            if re.search("writing", filepath):
                task = "writing"
            elif re.search("reading", filepath):
                task = "reading"

            dictionaries = init_variables(filepath, df)
            bb_start = dictionaries[0] 
            bb_dict = dictionaries[1]
            bb_dur_dict = dictionaries[2]
            aoi_start = dictionaries[3]
            aoi_dict = dictionaries[4]
            aoi_dur_dict = dictionaries[5]
            
            bb_dict, bb_dur_dict = process_df(bb_start+1, aoi_start, df, bb_dict, bb_dur_dict)
            aoi_dict, aoi_dur_dict = process_df(aoi_start, df.shape[1], df, aoi_dict, aoi_dur_dict)
            
            mean_aoi_durations = calculate_mean_fixation(aoi_dur_dict)
            mean_bb_durations = calculate_mean_fixation(bb_dur_dict)
            
            bb_dict.update(aoi_dict)
            mean_bb_durations.update(mean_aoi_durations)
            
            final_fix = {"pid" : p}
            final_dur = {"pid" : p}
            final_fix.update(bb_dict)
            final_dur.update(mean_bb_durations)

            # calculate_ratio(bb_dict, bb_dur_dict)
            # calculate_ratio(aoi_dict, aoi_dur_dict)
            
            fc_outpath = f"fixation_counts/{task}/{name}_fc.csv"
            fd_outpath = f"fixation_durations/{task}/{name}_fd.csv"

            with open(fc_outpath, "a+") as f:
                cw = csv.DictWriter(f, fieldnames = final_fix.keys())
                f.seek(0)
                # Check if the file is empty or if it does not exist, write the header
                if not f.read(1):
                    cw.writeheader()
                # cw.writeheader()
                cw.writerow(final_fix)
            
            with open(fd_outpath, "a+") as f:
                cw = csv.DictWriter(f, fieldnames = final_dur.keys())
                f.seek(0)
                # Check if the file is empty or if it does not exist, write the header
                if not f.read(1):
                    cw.writeheader()
                cw.writerow(final_dur)
                
            fc_outpath_both_tasks = f"fixation_counts/{name}_fc.csv"
            fd_outpath_both_tasks = f"fixation_durations/{name}_fd.csv"

            with open(fc_outpath_both_tasks, "a+") as f:
                cw = csv.DictWriter(f, fieldnames=final_fix.keys())
                f.seek(0)
                # Check if the file is empty or if it does not exist, write the header
                if not f.read(1):
                    cw.writeheader()
                # cw.writeheader()
                cw.writerow(final_fix)

            with open(fd_outpath_both_tasks, "a+") as f:
                cw = csv.DictWriter(f, fieldnames=final_dur.keys())
                f.seek(0)
                # Check if the file is empty or if it does not exist, write the header
                if not f.read(1):
                    cw.writeheader()
                cw.writerow(final_dur)

if __name__ == "__main__":
    main()

