import os
import csv
import pandas as pd
import tobii_research as tr
from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

### STIMULI 
arr = list(range(0, 5)) # list of indices 
#arr = list(range(0, 168)) # looking at all stimuli for testing purposes
writing_stimuli = pd.read_csv('./stimuli/writing_stimuli.csv') # stimuli --> snippets of code
reading_stimuli = pd.read_csv('./stimuli/reading_stimuli.csv') # stimuli --> snippets of code

# class for participant
class Participant_Info():
    pid = None
    first_task = None

# keeping track of task progress through different webpages
class Task_Progress():
    i = 0 # incrementer for writing task
    j = 0 # incrementer for reading task
    shuffled_arr = [] # basically a copy of arr, but shuffling this doesn't affect arr
    current_task = None
    progress = 0 # incremented as participant continues with task
    first_task_done = False

# Creates a directory for the participant and data files
# data files are:
# 1. keystrokes 
# 2. high-level task data (e.g. code summary ratings, summaries written)
def make_files(pid):
    global f_keystrokes, f_task, f_gaze_root
    path = 'data/%s'%str(pid)
    if os.path.exists(path):
        print('participant folder already exists')
    else:
        command = ('mkdir data/{pid}; mkdir data/{pid}/gaze/'.format(pid=pid))
        os.system(command)

    f_keystrokes = 'data/{pid}/{pid}_keystrokes.csv'.format(pid=pid)
    f_task = 'data/{pid}/{pid}_task.csv'.format(pid=pid)
    f_gaze_root = 'data/{pid}/gaze/{pid}_gaze'.format(pid=pid)
    # header for gaze files
    # ['participant_id', 'function_name', 'function_id', 'system_timestamp', 'device_timestamp', 'valid_gaze_left', 'valid_gaze_right', 'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 'valid_pd_right', 'gaze_left', 'gaze_right']

    # Writing headers
    with open(f_keystrokes, 'a+') as f:
        ctemp = csv.writer(f)
        ctemp.writerow(['participant_id', 'function_name', 'function_id', 'key_pressed', 'timestamp'])

    with open(f_task, 'a+') as f:
        ctemp = csv.writer(f)
        ctemp.writerow(['participant_id', 'function_name', 'function_id', 'task', 'summary', 'how_accurate', 
        'missing_info', 'unnecessary_info'])

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
    global arr, task, participant, writing_stimuli, reading_stimuli, f_gaze_root
    # Print gaze points of left and right eye
    system_timestamp = gaze_data['system_time_stamp']
    device_timestamp = gaze_data['device_time_stamp']
    gaze_validity_left = gaze_data['left_gaze_point_validity']
    gaze_validity_right = gaze_data['right_gaze_point_validity']
    gaze_left_eye = gaze_data['left_gaze_point_on_display_area']
    gaze_right_eye = gaze_data['right_gaze_point_on_display_area']
    valid_left_eye_pd = gaze_data['left_pupil_validity']
    valid_right_eye_pd = gaze_data['right_pupil_validity']
    pd_left = gaze_data['left_pupil_diameter']
    pd_right = gaze_data['right_pupil_diameter']
    # FIXME - how many stimuli to use
    # about 45s for reading, 1m for writing, break time for calibration
    # FIXME - restart progress if they quit in the middle
    # FIXME - check how bad the drifting is
    if task.current_task == "writing":
        fid = writing_stimuli.iloc[arr[task.i-1], 1]
        func_name = writing_stimuli.iloc[arr[task.i-1], 2]
    elif task.current_task == "reading":
            fid = reading_stimuli.iloc[arr[task.j-1], 1]
            func_name = reading_stimuli.iloc[arr[task.j-1], 2]
    gaze_file = "{root}_{func}_{fid}.csv".format(root=f_gaze_root, func=func_name, fid=fid)
    print("gaze file name", gaze_file)
    print("func name", func_name)

    with open(gaze_file, 'a+') as fg:
        cg = csv.writer(fg)
        cg.writerow([str(participant.pid), func_name, fid, system_timestamp, device_timestamp, gaze_validity_left, 
        gaze_validity_right, gaze_left_eye, gaze_right_eye, valid_left_eye_pd, valid_right_eye_pd, pd_left, pd_right])

# Start of UI, welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# FIXME: make HTML so they have to enter a value for pid
# instructions at the beginning of the experiment
@app.route('/instructions', methods=['POST'])
def instructions():
    global task, participant
    pid = request.form['pid'] # getting pid from HTML
    participant = Participant_Info() # creating object for participant and task progress
    participant.pid = pid
    participant.first_task = random.Random(pid).choice(['reading', 'writing']) # random choice whether reading/writing is first
    print("first task:", participant.first_task)
    
    task = Task_Progress()
    temp_arr = arr
    #random.Random(pid).shuffle(temp_arr) # random seeds for participants' task order
    task.shuffled_arr = temp_arr

    print("shuffled task:", task.shuffled_arr)
    make_files(pid) # and make folder/files for each participant
    
    if participant.first_task == "writing":
        return render_template('instructions.html', first_task = "writing")
    elif participant.first_task == "reading":
        return render_template('instructions.html', first_task = "reading")
      

# writing task
@app.route('/writing', methods=['POST'])
def writing():
    global arr, task, participant
    if task.current_task != "writing":
        task.current_task = "writing"

    task.i += 1 # preincrementing because can't increment after return render template
    
    if task.i == len(arr)+1: # end of writing stimuli has been reached
        fid = writing_stimuli.iloc[arr[task.i-2], 1] # identifying info for current function
        func_name = writing_stimuli.iloc[arr[task.i-2], 2]
        task.i = 0 # resetting writing incrementer
        summary = request.form['summary'] # summary written by participant

        with open(f_task, 'a+') as ft: # writing the last stimulus for participants
            cw = csv.writer(ft)
            cw.writerow([str(participant.pid), func_name, fid, "writing", summary, None, None, None])
        if task.first_task_done: # if participant has already done reading task, they've finished the experiment
            task.progress = 0 # resetting progress for next participant
            return render_template('goodbye.html')
        else: # halfway through
            task.first_task_done = True 
            task.progress = 50
            return render_template('rest.html', next_task="reading")
    else:
        if task.i > 1: # on first trial, participant won't have written a summary
            summary = request.form.get('summary')
            fid = writing_stimuli.iloc[arr[task.i-2], 1]
            func_name = writing_stimuli.iloc[arr[task.i-2], 2]
            with open(f_task, 'a+') as ft:
                cw = csv.writer(ft)
                cw.writerow([str(participant.pid), func_name, fid, "writing", summary, None, None, None])

        task.progress = task.progress + (1/(len(arr)))*50 # incrementing progress
        percent = task.progress
        return render_template('writing.html', code=writing_stimuli.iloc[arr[task.i-1], 5], percent=percent)

# Recording keystrokes during writing task
# Communicates with HTML function in writing.html
@app.route("/writing/submitkeystroke", methods=['GET', 'POST']) # FIXME - fix radio button bug
def submitkeystroke():
    global task, participant
    keypressed = request.args.get('keypressed')
    fid = writing_stimuli.iloc[arr[task.i-1], 1]
    func_name = writing_stimuli.iloc[arr[task.i-1], 2]

    # recording keystrokes along with function name and fid 
    with open(f_keystrokes, 'a+') as f:
        cw = csv.writer(f)
        cw.writerow([str(participant.pid), func_name, fid, chr(int(keypressed)), str(datetime.now())])
    return 'OK'

# break in between tasks
@app.route('/rest', methods=['POST'])
def rest():
    return render_template('rest.html')

# reading task
# basically the same logic as the writing task
# FIXME - center likert scale buttons
@app.route('/reading', methods=['POST'])
def reading(): 
    global arr, task, participant, reading_stimuli
    if task.current_task != "reading":
        task.current_task = "reading"
        
    task.j += 1
    print("j entering the loop:", task.j)
    if task.j == len(arr)+1:
        fid = reading_stimuli.iloc[arr[task.j-2], 1]
        func_name = reading_stimuli.iloc[arr[task.j-2], 2]
        task.j = 0
        accurate = request.form.get('accurate') # values from likert scale questions
        missing = request.form.get('missing')
        unnecessary = request.form.get('unnecessary')
        with open(f_task, 'a+') as ft:
            cw = csv.writer(ft)
            cw.writerow([str(participant.pid), func_name, fid, "reading", None, accurate, missing, unnecessary])
        if task.first_task_done:
            task.progress = 0
            return render_template('goodbye.html')
        else:
            task.first_task_done = True
            task.progress = 50
            return render_template('rest.html', next_task="writing")
    else:
        if task.j > 1:
            accurate = request.form.get('accurate') # values from likert scale questions
            missing = request.form.get('missing')
            unnecessary = request.form.get('unnecessary')
            fid = reading_stimuli.iloc[arr[task.j-2], 1]
            func_name = reading_stimuli.iloc[arr[task.j-2], 2]
            print("fid", fid)
            print("func name", func_name)
            with open(f_task, 'a+') as ft:
                cw = csv.writer(ft)
                cw.writerow([str(participant.pid), func_name, fid, "reading", None, accurate, missing, unnecessary])

        task.progress = task.progress + (1/(len(arr)))*50
        percent = task.progress
        code = reading_stimuli.iloc[arr[task.j-1], 5]
        human_summary = reading_stimuli.iloc[arr[task.j-1], 3]
        ai_summary = reading_stimuli.iloc[arr[task.j-1], 4]
        
        return render_template('reading.html', code=code, summary=random.choice([human_summary, ai_summary]), percent=percent) 
        
if __name__ == "__main__":
    
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
