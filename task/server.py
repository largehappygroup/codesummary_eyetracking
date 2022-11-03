import os
import csv
import time
import array
#from pickle import FALSE
import pandas as pd
#from symbol import pass_stmt
import tobii_research as tr
from flask import Flask, render_template, url_for, request
from flask import redirect, url_for
import random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

### STIMULI 
arr = list(range(0, 5)) # list of indices 
writing_stimuli = pd.read_csv('./stimuli/writing_stimuli.csv') # stimuli --> snippets of code
i = 0 # iterator for writing stimuli
reading_stimuli = pd.read_csv('./stimuli/reading_stimuli.csv') # stimuli --> snippets of code
j = 0 # iterator for reading stimuli 

### ENVIRONMENT VARIABLES
coinflip = None # deciding whether reading task is first or writing task is first
writing_done = False # 
reading_done = False # Bools for whether reading/writing task is finished

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


# Flip booleans for whether these tasks are done
def flip_writing_bool():
    global writing_done
    writing_done = True

def flip_reading_bool():
    global reading_done
    reading_done = True

### PARTICIPANT SPECIFIC 
# pseudorandomization for the experiment. It will be the same order for each pid.
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
    global f_keystrokes
    global f_task
    global f_gaze
    path = 'data/%s'%str(pid)
    if os.path.exists(path):
        print('participant folder already exists')
        #exit(1)
    else:
        command = ('mkdir data/%s' % str(pid))
        os.system(command)
    f_keystrokes = 'data/{pid}/keystrokes_{pid}.csv'.format(pid=pid)
    f_task = 'data/{pid}/task_{pid}.csv'.format(pid=pid)
    f_gaze = 'data/{pid}/gaze_{pid}.csv'.format(pid=pid)

### EYE-TRACKING
# setting up eye-tracker and making sure we can get data from it
def eye_tracker_setup():
    found_eyetrackers = tr.find_all_eyetrackers()
    if not found_eyetrackers:
        print('cannot find eyetracker')
        exit(1)
    else:
        my_eyetracker = found_eyetrackers[0]
    return my_eyetracker

# FIXME -- get more data from the eye tracker like validity, pupil diameter, etc.
def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    # FIXME Instead of print, write to a file
    # FIXME add more data
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))

# Start of UI, welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Recording keystrokes during writing task
# Communicates with HTML function in writing.html
@app.route("/writing/submitkeystroke", methods=['GET', 'POST'])
def submitkeystroke():
    keypressed = request.args.get('keypressed')
    with open(f_keystrokes, 'a+') as f:
        cw = csv.writer(f)
        cw.writerow([chr(int(keypressed)), str(datetime.now())])  # FIXME add something to record stimulus along with keystroke
    return 'OK'

# FIXME: make HTML so they have to enter a value for pid
# instructions at the beginning of the experiment
@app.route('/instructions', methods=['POST'])
def instructions():
    global i, j, arr, writing_stimuli, reading_stimuli, coinflip
    print("arr before shuffling\n", arr)
    pid = request.form['pid']
    arr = my_shuffle(arr, pid) # using PID at this point to shuffle stimuli 
    make_files(pid)            # and make folder/files for each participant
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
    global i, arr, writing_stimuli, reading_done
    i_increment()
    if i == len(arr)+1: # end of writing stimuli has been reached
        reset_i() # reset iterator through stimuli
        summary = request.form['summary'] # summary written by participant
        print(summary)
        if reading_done: # if participant has already done reading task
            return render_template('goodbye.html')
        else:
            flip_writing_bool() # writing is done, go on to reading
            return render_template('rest.html', next_task="reading")
    else:
        if i > 1: # on first trial, participant won't have written a summary
            summary = request.form['summary']
            print(summary)
        return render_template('writing.html', code=writing_stimuli.iloc[arr[i-1], 5])

# break in between tasks
@app.route('/rest', methods=['POST'])
def rest():
    return render_template('rest.html')

# reading task
# basically the same logic as the writing task
@app.route('/reading', methods=['POST'])
def reading():
    global j, arr, reading_stimuli, writing_done
    j_increment()
    if j == len(arr)+1:
        reset_j()
        acc = request.form['accurate']
        mis = request.form['missing']
        unn = request.form['unnecessary']
        if writing_done:
            return render_template('goodbye.html')
        else:
            flip_reading_bool()
            return render_template('rest.html', next_task="writing")
    else:
        if j > 1:
            acc = request.form['accurate']
            mis = request.form['missing']
            unn = request.form['unnecessary']
        human_summary = reading_stimuli.iloc[arr[j-1], 3]
        ai_summary = reading_stimuli.iloc[arr[j-1], 4]
        _code = reading_stimuli.iloc[arr[j-1], 5]
        return render_template('reading.html', code=_code, summary=random.choice([human_summary, ai_summary]))    
        
if __name__ == "__main__":
    # FIXME - add stuff for eyetracker
    #my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    app.run(host='0.0.0.0', port=8181, debug = True)
    #my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
