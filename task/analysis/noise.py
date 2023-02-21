import os
import re
import decimal
import pandas as pd

pid = 168


again = decimal.Decimal(72) / decimal.Decimal(7)
print(again)

def calculate_noise(root, eye_file):

    eye_file = pd.read_csv('{root}{eye_file}'.format(root=root, eye_file=eye_file), names=['participant_id', 'function_name', 'function_id', 'system_timestamp', 'device_timestamp', 'valid_gaze_left', 'valid_gaze_right', 'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 'valid_pd_right', 'pd_left', 'pd_right'])

    noise = 0
    half_noise = 0
    for i in range(eye_file.shape[0]):
        if (eye_file['valid_gaze_left'][i] == 0) and (eye_file['valid_gaze_right'][i] == 0):
            noise += 1
            continue
        elif (eye_file['valid_gaze_left'][i] == 0) or (eye_file['valid_gaze_right'][i] == 0):
            half_noise += 1
            continue
    
    with decimal.localcontext() as ctx:
        ctx.prec = 3
        all_noise = decimal.Decimal((half_noise+noise))/decimal.Decimal(eye_file.shape[0])
        print(all_noise)
        one_eye = decimal.Decimal(half_noise)/decimal.Decimal(eye_file.shape[0])
        neither_eye = decimal.Decimal(noise)/decimal.Decimal(eye_file.shape[0])
    
    return [all_noise, one_eye, neither_eye]
            
    
root = '../data/{pid}/gaze/'.format(pid=pid)
filelist = os.listdir(root)
filelen = len(filelist)
filelist.sort()
func_noise = []

for i in range(filelen):
    if re.search("reading", filelist[i]):
        task = "reading"
    elif re.search("writing", filelist[i]):
        task = "writing"
    func = re.search('_[a-zA-Z0-9]*\.csv', filelist[i])
    func = func[0][1:-4]

    all_noise, one_eye, neither_eye = calculate_noise(root, filelist[i])
    func_noise.append([func, all_noise, one_eye, neither_eye])
    
func_noise = pd.DataFrame(func_noise, columns=["function", "all_noise", "one_eye_valid", "neither_eyes_valid"])
pd.DataFrame.to_csv(func_noise, "../data/{pid}/{pid}_noise_report.csv".format(pid=pid))
    
