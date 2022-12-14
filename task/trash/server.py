######################
##### DEPRECATED #####
######################

import os
import csv
import time
import array
import pandas as pd
import tobii_research as tr
from flask import Flask, render_template, url_for, request
from flask import redirect, url_for
import random
from datetime import datetime

app = Flask(__name__)

### STIMULI 
arr = list(range(0, 5)) # list of indices 
writing_stimuli = pd.read_csv('./stimuli/writing_stimuli.csv') # stimuli --> snippets of code
i = 0 # iterator for writing stimuli
reading_stimuli = pd.read_csv('./stimuli/reading_stimuli.csv') # stimuli --> snippets of code
j = 0 # iterator for reading stimuli 

# FIXME - data logged innaccurately --> issue with iterator and logging for func_name, fid

### ENVIRONMENT VARIABLES
coinflip = None # deciding whether reading task is first or writing task is first
writing_done = False # 
reading_done = False # Bools for whether reading/writing task is finished
current_task = None
progress = 0
pid = None

### ITERATOR FUNCTIONS
# incrementing the iterator for writing stimuli
def i_increment(): 
    global i 
    i += 1

# incrementing the iterator for reading stimuli
def j_increment():
    global j
    j += 1

# resetting at the end of the task --> prevents some errors about going back, restarting, etc
def reset_i():
    global i
    i = 0

def reset_j():
    global j
    j = 0
    
def reset_arr():
    global arr
    arr = list(range(0, 5))
    
def set_current_task(task):
    global current_task
    current_task = task

# editing the global progress variable once the participant completes half the experiment
def halfway():
    global progress
    progress = 50

def reset_progress():
    global progress
    progress = 0

# Flip booleans for whether these tasks are done
def flip_writing_bool():
    global writing_done
    writing_done = True

def flip_reading_bool():
    global reading_done
    reading_done = True

### PARTICIPANT SPECIFIC 
# pseudorandomization for the experiment. It will be the same order for each pid.
def set_pid(_pid):
    global pid
    pid = _pid
    print("pid", pid)
    print("_pid", _pid)

def my_shuffle(array, pid):
    global coinflip
    coinflip = random.Random(pid).randint(0, 1)
    random.Random(pid).shuffle(array)
    return array

# Creates a directory for the participant and data files
# data files are:
# 1. keystrokes 
# 2. high-level task data (e.g. code summary ratings, summaries written)
def make_files(pid):
    global f_keystrokes, f_task, f_gaze
    path = 'data/%s'%str(pid)
    if os.path.exists(path):
        print('participant folder already exists')
        #exit(1)
    else:
        command = ('mkdir data/%s' % str(pid))
        os.system(command)
    print(pid)
    f_keystrokes = 'data/{pid}/{pid}_keystrokes.csv'.format(pid=pid)
    f_task = 'data/{pid}/{pid}_task.csv'.format(pid=pid)
    f_gaze = 'data/{pid}/{pid}_gaze.csv'.format(pid=pid)

    # Writing headers
    with open(f_keystrokes, 'a+') as f:
        ctemp = csv.writer(f)
        ctemp.writerow(['participant_id', 'function_name', 'function_id', 'key_pressed', 'timestamp'])

    with open(f_task, 'a+') as f:
        ctemp = csv.writer(f)
        ctemp.writerow(['participant_id', 'function_name', 'function_id', 'task', 'summary', 'how_accurate', 
        'missing_info', 'unnecessary_info'])

    with open(f_gaze, 'a+') as f:
        ctemp = csv.writer(f)
        ctemp.writerow(['participant_id', 'function_name', 'function_id', 'valid_gaze_left', 'valid_gaze_right', 'gaze_left_eye',
        'gaze_right_eye', 'valid_pd_left', 'valid_pd_right', 'gaze_left', 'gaze_right'])

### EYE-TRACKING
# setting up eye-tracker and making sure we can get data from it
def eye_tracker_setup():
    found_eyetrackers = tr.find_all_eyetrackers()
    if not found_eyetrackers:
        print('cannot find eyetracker')
    else:
        my_eyetracker = found_eyetrackers[0]
    return my_eyetracker

def tobii_data_callback(gaze_data):
    global i, j, arr, pid, writing_stimuli, reading_stimuli
    # Print gaze points of left and right eye
    system_timestamp = gaze_data['system_time_stamp']
    device_timestamp = gaze_data['device_time_stamp']
    gaze_validity_left = gaze_data['left_gaze_point_validity']
    gaze_validity_right = gaze_data['right_gaze_point_validity']
    gaze_left_eye = gaze_data['left_gaze_point_on_display_area']
    #gaze_left_eye_coordinate = gaze_data['left_gaze_point_in_user_coordinate_system'] # user coordinate system also tracks distance from the eye-tracker
    gaze_right_eye = gaze_data['right_gaze_point_on_display_area']
    #gaze_right_eye_coordinate = gaze_data['right_gaze_point_in_user_coordinate_system']
    valid_left_eye_pd = gaze_data['left_pupil_validity']
    valid_right_eye_pd = gaze_data['right_pupil_validity']
    pd_left = gaze_data['left_pupil_diameter']
    pd_right = gaze_data['right_pupil_diameter']
    # FIXME - split up gaze file by function pid_fid_gaze.csv
    # FIXME - figure out how to tell whether they're on writing or reading
    # FIXME - how many stimuli to use
    # about 45s for reading, 1m for writing, break time for calibration
    # FIXME - restart progress if they quit in the middle
    # FIXME - check how bad the drifting is
    if current_task == "writing":
        fid = writing_stimuli.iloc[arr[i-1], 1]
        func_name = writing_stimuli.iloc[arr[i-1], 2]
    elif current_task == "reading":
            fid = reading_stimuli.iloc[arr[j-1], 1]
            func_name = reading_stimuli.iloc[arr[j-1], 2]

    with open(f_gaze, 'a+') as fg:
        cg = csv.writer(fg)
        cg.writerow([str(pid), func_name, fid, system_timestamp, device_timestamp, gaze_validity_left, 
        gaze_validity_right, gaze_left_eye, gaze_right_eye, valid_left_eye_pd, valid_right_eye_pd, pd_left, pd_right])

# Start of UI, welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# FIXME: make HTML so they have to enter a value for pid
# instructions at the beginning of the experiment
@app.route('/instructions', methods=['POST'])
def instructions():
    global i, j, arr, pid, writing_stimuli, reading_stimuli, coinflip
    print("arr before shuffling\n", arr)
    _pid = request.form['pid']
    set_pid(_pid)
    arr = my_shuffle(arr, _pid) # using PID at this point to shuffle stimuli 
    make_files(_pid)            # and make folder/files for each participant
    print("arr after shuffling\n", arr)
    # writing is first
    if coinflip == 1: 
        return render_template('instructions.html', first_task = "writing")
    # reading is first
    elif coinflip == 0:
        return render_template('instructions.html', first_task = "reading")

# writing task
@app.route('/writing', methods=['POST'])
def writing():
    global i, arr, pid, current_task, writing_stimuli, reading_done, progress
    if current_task != "writing":
        set_current_task("writing")
        
    i_increment()
    if i == len(arr)+1: # end of writing stimuli has been reached
        reset_i() # reset iterator through stimuli
        print("i:", i)
        fid = writing_stimuli.iloc[arr[i-1], 1]
        func_name = writing_stimuli.iloc[arr[i-1], 2]

        summary = request.form['summary'] # summary written by participant
        #print(summary)

        with open(f_task, 'a+') as ft:
            cw = csv.writer(ft)
            cw.writerow([str(pid), func_name, fid, "writing", summary, None, None, None])
        if reading_done: # if participant has already done reading task
            reset_progress()
            reset_arr()
            return render_template('goodbye.html')
        else:
            flip_writing_bool() # writing is done, go on to reading
            halfway() # setting progress bar to 50%
            return render_template('rest.html', next_task="reading")
    else:
        if i > 1: # on first trial, participant won't have written a summary
            summary = request.form.get('summary')
            fid = writing_stimuli.iloc[arr[i-1], 1]
            func_name = writing_stimuli.iloc[arr[i-1], 2]
            with open(f_task, 'a+') as ft:
                cw = csv.writer(ft)
                cw.writerow([str(pid), func_name, fid, "writing", summary, None, None, None])
            #print(summary)
        
        _percent = progress + (i/(len(arr)))*50
        return render_template('writing.html', code=writing_stimuli.iloc[arr[i-1], 5], percent=_percent)

# Recording keystrokes during writing task
# Communicates with HTML function in writing.html
@app.route("/writing/submitkeystroke", methods=['GET', 'POST']) # FIXME - fix radio button bug
def submitkeystroke():
    global pid
    keypressed = request.args.get('keypressed')
    fid = writing_stimuli.iloc[arr[i-1], 1]
    func_name = writing_stimuli.iloc[arr[i-1], 2]

    # recording keystrokes along with function name and fid 
    with open(f_keystrokes, 'a+') as f:
        cw = csv.writer(f)
        cw.writerow([str(pid), func_name, fid, chr(int(keypressed)), str(datetime.now())])
    return 'OK'

# break in between tasks
@app.route('/rest', methods=['POST'])
def rest():
    return render_template('rest.html')

# reading task
# basically the same logic as the writing task
@app.route('/reading', methods=['POST'])
def reading(): 
    global j, arr, pid, current_task, reading_stimuli, writing_done, progress
    j_increment()
    if current_task != "reading":
        set_current_task("reading")
    if j == len(arr)+1:

        reset_j()
        fid = reading_stimuli.iloc[arr[j-1], 1]
        func_name = reading_stimuli.iloc[arr[j-1], 2]
        accurate = request.form.get('accurate') # values from likert scale questions
        missing = request.form.get('missing')
        unnecessary = request.form.get('unnecessary')
        with open(f_task, 'a+') as ft:
            cw = csv.writer(ft)
            cw.writerow([str(pid), func_name, fid, "reading", None, accurate, missing, unnecessary])
        if writing_done:
            reset_progress()
            reset_arr()
            return render_template('goodbye.html')
        else:
            flip_reading_bool()
            halfway() # setting progress bar to half
            return render_template('rest.html', next_task="writing")
    else:
        if j > 1:
            accurate = request.form.get('accurate') # values from likert scale questions
            missing = request.form.get('missing')
            unnecessary = request.form.get('unnecessary')
            fid = reading_stimuli.iloc[arr[j-1], 1]
            func_name = reading_stimuli.iloc[arr[j-1], 2]
            with open(f_task, 'a+') as ft:
                cw = csv.writer(ft)
                cw.writerow([str(pid), func_name, fid, "reading", None, accurate, missing, unnecessary])

        _percent = progress + (j/(len(arr)))*50
        human_summary = reading_stimuli.iloc[arr[j-1], 3]
        ai_summary = reading_stimuli.iloc[arr[j-1], 4]
        _code = reading_stimuli.iloc[arr[j-1], 5]
        return render_template('reading.html', code=_code, summary=random.choice([human_summary, ai_summary]), percent=_percent) 
        
if __name__ == "__main__":
    global starttime # FIXME - get delta time
    # trying to connect to eyetracker
    try:
        my_eyetracker = eye_tracker_setup()
        my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, tobii_data_callback, as_dictionary=True)
    except:
        UnboundLocalError("WARNING: couldn't find eyetracker")
    
    # start server
    app.run(host='0.0.0.0', port=8181, debug = True)
    try:
        my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, tobii_data_callback)
    except:
        UnboundLocalError("WARNING: no eyetracker, but experiment has ended")
