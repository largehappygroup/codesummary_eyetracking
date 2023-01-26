import os
import csv
import math
import random
import pandas as pd
import tobii_research as tr
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
# FIXME - make a save point
# FIXME - pseudorandomize human written/ai written
# FIXME - unsubscribe from eye-tracker during breaks

### STIMULI 
#arr = list(range(0, 5)) # list of indices 
arr = list(range(0, 167)) # looking at all stimuli for testing purposes
writing_arr = list(range(0, 16)) # 60% plus one that gets eaten up by the rest trial
reading_arr = list(range(0, 28)) # 60%
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
    at_rest = False
    current_task = None
    progress = 0 # incremented as participant continues with task
    first_task_done = False
    is_finished = False

# Creates a directory for the participant and data files
# data files are:
# 1. keystrokes 
# 2. high-level task data (e.g. code summary ratings, summaries written)
def make_files(pid):
    global f_keystrokes, f_task, f_gaze_root, f_writing_save, f_reading_save
    path = 'data/%s'%str(pid)
    if os.path.exists(path):
        print('participant folder already exists')
    else:
        command = ('mkdir data/{pid}; mkdir data/{pid}/gaze/'.format(pid=pid))
        os.system(command)

    f_keystrokes = 'data/{pid}/{pid}_keystrokes.csv'.format(pid=pid)
    f_task = 'data/{pid}/{pid}_task.csv'.format(pid=pid)
    f_gaze_root = 'data/{pid}/gaze/{pid}_gaze'.format(pid=pid)
    f_writing_save = 'data/{pid}/{pid}_writing_save.csv'.format(pid=pid)
    f_reading_save = 'data/{pid}/{pid}_reading_save.csv'.format(pid=pid)
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
    global arr, task, participant, writing_stimuli, reading_stimuli, f_gaze_root, gaze_file
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
    # FIXME - restart progress if they quit in the middle
    # FIXME - check how bad the drifting is
    if task.current_task == "writing":
        fid = writing_stimuli.iloc[arr[task.i-1], 1]
        func_name = writing_stimuli.iloc[arr[task.i-1], 2]
    elif task.current_task == "reading":
            fid = reading_stimuli.iloc[arr[task.j-1], 1]
            func_name = reading_stimuli.iloc[arr[task.j-1], 2]
    gaze_file = "{root}_{func}.csv".format(root=f_gaze_root, func=func_name)
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
    global task, participant, writing_arr, reading_arr, f_writing_save, f_reading_save
    pid = request.form['pid'] # getting pid from HTML
    participant = Participant_Info() # creating object for participant and task progress
    participant.pid = pid
    task = Task_Progress()
    
    # finalizing participant's stimuli
    variable_writing = random.Random(pid).sample(range(16, 74), 10) # change the last number in this line to +/- stimuli to writing task
    variable_reading = random.Random(pid).sample(range(28, 93), 18) # change the last number in this line to +/- stimuli to the reading task
    if not task.is_finished:
        writing_arr = writing_arr + variable_writing
        reading_arr = reading_arr + variable_reading
    random.Random(pid).shuffle(writing_arr)
    random.Random(pid).shuffle(reading_arr)
    print("after shuffling")
    print("writing", len(writing_arr), writing_arr)
    print("reading", len(reading_arr), reading_arr)
    make_files(pid)  # and make folder/files for each participant
    participant.first_task = random.Random(pid).choice(['reading', 'writing'])

    try:
        writing_save = pd.read_csv(f_writing_save)
        w_checkpoint = writing_save.columns[0]
        task.i = int(w_checkpoint)
        if task.i > len(writing_arr)+1 and participant.first_task == "writing":
            task.first_task_done == True
            participant.first_task = "reading"
    except:
        print("This checkpoint for writing doesn't exist yet")
    
    try:
        reading_save = pd.read_csv(f_reading_save)
        r_checkpoint = reading_save.columns[0]
        task.j = int(r_checkpoint)
        if task.j > len(reading_arr)+1 and participant.first_task == "reading":
            task.first_task_done == True
            participant.first_task = "writing"
    except:
        print("This checkpoint for reading doesn't exist yet")
        
    # random choice whether reading/writing is first

    print("first task:", participant.first_task)
    
    if participant.first_task == "writing":
        return render_template('instructions.html', first_task = "writing")
    elif participant.first_task == "reading":
        return render_template('instructions.html', first_task = "reading")

# writing task
@app.route('/writing', methods=['POST'])
def writing():
    global writing_arr, task, participant, f_writing_save
    if task.current_task != "writing":
        task.current_task = "writing"
    
    if task.at_rest == True:
        task.i += 1
        try:
            my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, tobii_data_callback, as_dictionary=True)
        except:
            UnboundLocalError("WARNING: couldn't find eyetracker")
        task.at_rest = False
        
    if task.i == math.floor((len(writing_arr)+1)/2):
        task.at_rest = True
        try:
            my_eyetracker.unsubscribe_from(
                tr.EYETRACKER_GAZE_DATA, tobii_data_callback)  # stop recording gaze data
        except:
            UnboundLocalError("WARNING: no eyetracker, but resting")
        return render_template('rest.html', next_task="writing")
        
    task.i += 1 # preincrementing because can't increment after return render template
    # Halfway through writing task, take a break
    with open(f_writing_save, "w") as f:
        f.write(str(task.i))
    
    if task.i == len(writing_arr)+1: # end of writing stimuli has been reached
        fid = writing_stimuli.iloc[writing_arr[task.i-2], 1] # identifying info for current function
        func_name = writing_stimuli.iloc[writing_arr[task.i-2], 2]
        summary = request.form['summary'] # summary written by participant
        task.i = 0 # resetting writing incrementer

        with open(f_task, 'a+') as ft: # writing the last stimulus for participants
            cw = csv.writer(ft)
            cw.writerow([str(participant.pid), func_name, fid, "writing", summary, None, None, None])
        if task.first_task_done: # if participant has already done reading task, they've finished the experiment
            task.progress = 0 # resetting progress for next participant
            task.is_finished = True
            try:
                my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, tobii_data_callback)
            except:
                UnboundLocalError("WARNING: no eyetracker, but experiment has ended")
            return render_template('goodbye.html')
        else: # halfway through
            task.first_task_done = True 
            task.progress = 50
            return render_template('rest.html', next_task="reading")
    else:
        if task.i > 1: # on first trial, participant won't have written a summary
            summary = request.form.get('summary')
            fid = writing_stimuli.iloc[writing_arr[task.i-2], 1]
            func_name = writing_stimuli.iloc[writing_arr[task.i-2], 2]
            with open(f_task, 'a+') as ft:
                cw = csv.writer(ft)
                cw.writerow([str(participant.pid), func_name, fid, "writing", summary, None, None, None])

        task.progress = task.progress + (1/(len(writing_arr)))*50 # incrementing progress
        percent = task.progress
        return render_template('writing.html', code=writing_stimuli.iloc[writing_arr[task.i-1], 5], percent=percent)

# Recording keystrokes during writing task
# Communicates with HTML function in writing.html
@app.route("/writing/submitkeystroke", methods=['GET', 'POST']) # FIXME - fix radio button bug
def submitkeystroke():
    global task, participant, writing_arr
    keypressed = request.args.get('keypressed')
    fid = writing_stimuli.iloc[writing_arr[task.i-1], 1]
    func_name = writing_stimuli.iloc[writing_arr[task.i-1], 2]

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
    global reading_arr, task, participant, reading_stimuli, my_eyetracker, f_reading_save
    if task.current_task != "reading":
        task.current_task = "reading"
        
    if task.at_rest == True:
        task.j += 1
        try:
            my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, tobii_data_callback, as_dictionary=True)
        except:
            UnboundLocalError("WARNING: couldn't find eyetracker")
        task.at_rest = False
        
    if task.j == math.floor((len(reading_arr)+1)/2):
        task.at_rest = True
        try:
            my_eyetracker.unsubscribe_from(
                tr.EYETRACKER_GAZE_DATA, tobii_data_callback)
        except:
            UnboundLocalError("WARNING: no eyetracker, but resting")
        return render_template('rest.html', next_task="reading")
    
    task.j += 1
    with open(f_reading_save, "w") as f:
        f.write(str(task.j))
    
    if task.j == len(reading_arr)+1:
        fid = reading_stimuli.iloc[reading_arr[task.j-2], 1]
        func_name = reading_stimuli.iloc[reading_arr[task.j-2], 2]
        accurate = request.form.get('accurate') # values from likert scale questions
        missing = request.form.get('missing')
        unnecessary = request.form.get('unnecessary')
        task.j = 0
            
        with open(f_task, 'a+') as ft:
            cw = csv.writer(ft)
            cw.writerow([str(participant.pid), func_name, fid, "reading", None, accurate, missing, unnecessary])
            
        if task.first_task_done:
            task.progress = 0
            task.is_finished = True
            try:
                my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, tobii_data_callback)
            except:
                UnboundLocalError("WARNING: no eyetracker, but experiment has ended")
                
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
            fid = reading_stimuli.iloc[reading_arr[task.j-2], 1]
            func_name = reading_stimuli.iloc[reading_arr[task.j-2], 2]
            print("fid", fid)
            print("func name", func_name)
            with open(f_task, 'a+') as ft:
                cw = csv.writer(ft)
                cw.writerow([str(participant.pid), func_name, fid, "reading", None, accurate, missing, unnecessary])

        task.progress = task.progress + (1/(len(reading_arr)))*50
        percent = task.progress
        code = reading_stimuli.iloc[reading_arr[task.j-1], 5]
        human_summary = reading_stimuli.iloc[reading_arr[task.j-1], 3]
        ai_summary = reading_stimuli.iloc[reading_arr[task.j-1], 4]
        
        return render_template('reading.html', code=code, summary=random.choice([human_summary, ai_summary]), percent=percent) 
        
        
if __name__ == "__main__":
    global my_eyetracker
    
    try:
        my_eyetracker = eye_tracker_setup()
        my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, tobii_data_callback, as_dictionary=True)
    except:
        UnboundLocalError("WARNING: couldn't find eyetracker")
    
    # start server
    app.run(host='0.0.0.0', port=8181, debug = True)
