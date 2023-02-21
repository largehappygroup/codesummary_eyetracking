import os
import re
from datetime import datetime
import pandas as pd
import numpy as np

# CSV directory
pid = 143
dir = '../data/{pid}/gaze/'.format(pid=pid)
dirlist = os.listdir(dir)

system_timelist = []
device_timelist = []
for file in dirlist:
    func = re.search('_[a-zA-Z0-9]*\.csv', file)
    func = func[0][1:-4]
    if re.search("reading", file):
        task = "reading"
    elif re.search("writing", file):
        task = "writing"
    print(func, task)
    df = pd.read_csv(str(dir+file), names=['participant_id', 'function_name', 'function_id', 'system_timestamp', 'device_timestamp', 'valid_gaze_left', 'valid_gaze_right', 'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 'valid_pd_right', 'pd_left', 'pd_right'])
    sys_start = df['system_timestamp'][0]/10**6
    sys_end = df['system_timestamp'][len(df)-1]/10**6
    dev_start = df['device_timestamp'][0]/10**6
    dev_end = df['device_timestamp'][len(df)-1]/10**6
    system_timelist.append([sys_start, func, task, sys_end])
    device_timelist.append([dev_start, func, task, dev_end])
    
    # print("system start timestamp:", df['system_timestamp'][0]/10**6)
    # print("device start timestamp", df['device_timestamp'][0]/10**6)
    # print("system end timestamp:", df['system_timestamp'][len(df)-1]/10**6)
    # print("device end timestamp:", df['device_timestamp'][len(df)-1]/10**6)
    print("system diff:", (df['system_timestamp'][len(df)-1]/10**6) - (df['system_timestamp'][0]/10**6))
    print("device diff:", (df['device_timestamp'][len(df)-1]/10**6) - (df['device_timestamp'][0]/10**6))

print(sorted(system_timelist))
print(sorted(device_timelist))
system_timelist = sorted(system_timelist)
device_timelist = sorted(device_timelist)

for i, tup in enumerate(system_timelist):
    if i != (len(system_timelist)-1):
        diff = system_timelist[i+1][0]-tup[3]
        print(diff)
        
total_time = (system_timelist[len(system_timelist)-1][3] - system_timelist[0][0])/60
print("total time", total_time)
# find first time, find final time
# sort
# find lag between tasks