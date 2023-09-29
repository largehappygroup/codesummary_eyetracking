import os
import re
import pickle
import numpy as np
import pandas as pd

with open("midprocessing/function_tokens.pkl", "rb") as f:
    function_tokens = pickle.load(f)
with open("midprocessing/ASTs.pkl", "rb") as f:
    trees = pickle.load(f)
with open("midprocessing/to_toss.pkl", "rb") as f:
    to_toss = pickle.load(f)


def init_variables(filepath, df):
    aoi_start = -1
    if re.search("reading", filepath):
        aoi_start = df.columns.get_loc('prewritten')
    elif re.search("writing", filepath):
        aoi_start = df.columns.get_loc('code')
    bb_start = df.columns.get_loc("geometry")
    return [bb_start, aoi_start]

# preprocess function to downsample and narrow down to just bounding boxes


def preprocess(fullpath, downsample):
    gazedf = pd.read_csv(fullpath)
    if downsample:
        gazedf = gazedf[::2]  # downsample
        gazedf = gazedf.reset_index(drop=True)

    # get just the rows where participant was looking at code
    codedf = gazedf[gazedf['code'] == 1]
    codedf = codedf.reset_index(drop=True)
    return codedf

# print function might give trouble
# filter out all gaze points that aren't in the code
# return
def calculate_scan_path(filepath, codedf):
    bb_start, aoi_start = init_variables(filepath, codedf)
    bbdf = codedf.iloc[:, bb_start+1:aoi_start]
    scan_path = []
    count = 0  # used for calculating regressions later on
    curr_token = ''
    for i, row in bbdf.iterrows():
        index = np.where(row == 1)[0]
        if len(index) > 0:
            token = bbdf.columns[index][0]
            if token != curr_token:
                scan_path.append(token)
                curr_token = token
            else:
                count += 1
    return scan_path, count


participants = "FIXME" # Ask Zach Karas for access to data

rscan_paths = {}
wscan_paths = {}
scan_path_per_person = {}
reading_functions = set()
writing_functions = set()
non_regressions = {}

for person in participants:
    print(person)
    scan_path_per_person[person] = {}
    metadir = "FIXME" # Ask Zach for this one too
    gaze_files = os.listdir(metadir)
    downsample = True if int(person) < 300 else False
    non_regressions[person] = {}
    for file in gaze_files:
        name = file.split('_')[-1]
        name = re.sub(".csv", "", name)

        # if this person's data needs to be excluded for this file
        if name in to_toss.keys() and int(person) in to_toss[name]:
            continue

        fullpath = f"{metadir}/{file}"

        preprocessed = preprocess(fullpath, downsample)
        scan_path, count = calculate_scan_path(file, preprocessed)
        scan_path_per_person[person][name] = scan_path
        non_regressions[person][name] = count

        if re.search("writing", file):
            writing_functions.add(name)
            if name not in wscan_paths:
                wscan_paths[name] = [scan_path]
            else:
                wscan_paths[name].append(scan_path)
        elif re.search("reading", file):
            reading_functions.add(name)
            if name not in rscan_paths:
                rscan_paths[name] = [scan_path]
            else:
                rscan_paths[name].append(scan_path)

    # print(len(scan_path_per_person))
    # break

# with open("midprocessing/reading_scanpaths.pkl", "wb") as f:
#     pickle.dump(rscan_paths, f)

# with open("midprocessing/writing_scanpaths.pkl", "wb") as f:
#     pickle.dump(wscan_paths, f)

# with open("midprocessing/participant_scanpaths.pkl", "wb") as f:
#     pickle.dump(scan_path_per_person, f)

# with open("midprocessing/reading_functions.pkl", "wb") as f:
#     pickle.dump(reading_functions, f)

# with open("midprocessing/writing_functions.pkl", "wb") as f:
#     pickle.dump(writing_functions, f)
