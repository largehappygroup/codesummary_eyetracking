import os
import re
import pickle
import statistics
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon


Bounding_Boxes = {} # dictionary that holds geopandas shapes of all bounding boxes
height = 1080 # height of computer screen
width = 1920 # width of computer screen

# normalizing to be between 0-1 
# tobii eye-tracker calculates gaze point in 0-1
def normalize_coordinates(x, y, w, h):
    global width
    global height
    x /= width
    y /= height
    w /= width
    h /= height
    return x, y, w, h
    
# checks whether bounding box is already in dictionary,
# otherwise this turns the bounding box coordinates into 
# a GeoSeries of rectangle shapes.
# Later, the gaze coordinate will be matched to these boxes.
def make_shapes(filename):
    global Bounding_Boxes
    name = filename.split("_")[3]
    name = f"{name}.csv"
    
    if name in Bounding_Boxes:
        return Bounding_Boxes[name]
    else:
        ref = pd.read_csv(f'../analysis/fully_annotated/{name}')
        boxes = pd.DataFrame()

        for i in range(len(ref)): # creating shapes for each word in the file
            x = float(ref.loc[i, 'tobii_x'])
            y = float(ref.loc[i, 'tobii_y'])
            w = float(ref.loc[i, 'tobii_width'])
            h = float(ref.loc[i, 'tobii_height'])
            word = '{word}.{num}'.format(word=ref.loc[i, 'word'], num=ref.loc[i, 'occurrence'])
            # Creating a shape for each word based on its coordinates
            new_tangle = pd.Series({word: Polygon([(x, y), (x+w, y), (x, y+h), (x+w, y+h)])}) 
            boxes = pd.concat([boxes, new_tangle]) # adding this to a new data structure 
        Bounding_Boxes[name] = boxes
        return boxes

# In addition to the bounding boxes, here I'm adding 
# Areas of interest for the reading questions, the participants'
# summaries, and the code. This is just run once.
def make_aois():
    aois = [(1175, 200, 700, 125),  # prewritten summary
            (1175, 450, 600, 100),  # 'accurate' question
            (1175, 550, 600, 150),  # 'missing' question
            (1175, 725, 600, 100),  # 'unnecessary' question
            (1175, 825, 600, 125),  # 'readable' question
            (0,    85, 1160, 975),  # code
            (1175, 85,  720, 300)]  # participant summary

    tobii_aois = []
    aoi_names = ['prewritten', 'accurate', 'missing', 'unnecessary', 'readable', 'code']
    writing_aoi_names = ['code', 'participant_summary']

    for box in aois:
        x, y, w, h = normalize_coordinates(box[0], box[1], box[2], box[3])
        tobii_aois.append((x, y, w, h))
        
    reading_boxes = pd.DataFrame()
    for i in range(len(aoi_names)):
        x = tobii_aois[i][0] 
        y = tobii_aois[i][1]
        w = tobii_aois[i][2]
        h = tobii_aois[i][3]
        new_tangle = pd.Series({aoi_names[i]: Polygon([(x, y), (x+w, y), (x, y+h), (x+w, y+h)])})
        reading_boxes = pd.concat([reading_boxes, new_tangle])
    
    writing_boxes = pd.DataFrame()
    for i in range(len(writing_aoi_names)):
        x = tobii_aois[i+5][0]
        y = tobii_aois[i+5][1]
        w = tobii_aois[i+5][2]
        h = tobii_aois[i+5][3]
        new_tangle = pd.Series({writing_aoi_names[i]: Polygon([(x, y), (x+w, y), (x, y+h), (x+w, y+h)])})
        writing_boxes = pd.concat([writing_boxes, new_tangle])
    
    return reading_boxes, writing_boxes


# takes coordinate for left and right eye,
# then averages them to get gaze point.
# Returns a geopandas point
def get_gaze_point(row):
    gaze_left = row['gaze_left_eye']
    gaze_right = row['gaze_right_eye']
    temp_left = re.split(r'[(,\)]', gaze_left) # tuple is a string, so using regex to get the numbers
    temp_right = re.split(r'[(,\)]', gaze_right)
    
    # averaging right and left gaze points for one gaze point
    gaze_point = (statistics.fmean([float(temp_left[1]), float(temp_right[1])]), 
                 statistics.fmean([float(temp_left[2]), float(temp_right[2])]))
    if pd.isna(gaze_point[0]) or pd.isna(gaze_point[1]): # if either eye is invalid
        return -1
    else:
        return [Point(gaze_point[0], gaze_point[1])]

# assigning point to a box and/or aoi
# this is the most computationally expensive part
def localize_gaze(gaze_point, row, boxes):
    pnt = gpd.GeoDataFrame(geometry=gaze_point)
    # confusing, but basically this below line returns false/true whether the point is in a shape
    pnt = pnt.assign(**{key: pnt.within(geom) for key, geom in boxes.items()}) 
    temp = pd.DataFrame(pnt)
    temp = temp.replace({True : 1, False : ''}) # converting 'True' and 'False' to 1 and nothing
    return pd.concat([row, temp.T]) # adding this true/false information to the original row


def main():
    global Bounding_Boxes
    # folder where all of participants' gaze data is stored 
    gaze_files = os.listdir("/home/zachkaras/pickle_data")
    reading_aois, writing_aois = make_aois() # running this once to make boxes for AOIs
    
    for file in gaze_files: # for each participant
        pid = re.sub("_all.pkl", "", file)
        # path for output
        path = f"/home/zachkaras/code_summ_data/{pid}/annotated_gaze"
        try:
            os.mkdir(path)
        except:
            print("folder already exists")
        
        # eyetracking files
        eye_file = open(f"/home/zachkaras/pickle_data/{file}", "rb")
        
        contents = pickle.load(eye_file)
        all_files = dict() # will store all participant's files as a pkl file

        for key,values in contents.items(): # iterating through all participant's gaze files
            print(key)    
            boxes = make_shapes(key)
            if re.search("reading", key):
                boxes = pd.concat([boxes, reading_aois])
            elif re.search("writing", key):
                boxes = pd.concat([boxes, writing_aois])
            
            boxes = gpd.GeoSeries(boxes[0]) # turning boxes into geopandas object
            
            df = pd.DataFrame.from_dict(values).T
            num_cols = len(df.columns)
            if num_cols == 14: # older files didn't include data for distance from eye-tracker
                df.columns = ['participant_id', 'function_name', 'function_id', 'system_timestamp',
                                    'device_timestamp', 'valid_gaze_left', 'valid_gaze_right', 
                                    'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 'valid_pd_right',
                                    'pd_left', 'pd_right', 'fixation']
            elif num_cols == 18:
                df.columns = ['participant_id', 'function_name', 'function_fid', 'system_timestamp',
                                    'device_timestamp', 'valid_gaze_left', 'valid_gaze_right', 
                                    'gaze_left_eye', 'gaze_right_eye', 'valid_pd_left', 'valid_pd_right',
                                    'pd_left', 'pd_right', 'irl_left_eye_coordinates', 
                                    'irl_right_eye_coordinates', 'irl_left_point_on_screen', 
                                    'irl_right_point_on_screen', 'fixation']
            else:
                #print(f"weird column length. Participant: {file} | File: {key} | # Columns: {num_cols}")
                continue # the only files without 14 or 18 columns have 0 columns

            # iterate through each file, get gaze point
            new_df = pd.DataFrame()
            for i, row in df.iterrows(): # through each gaze file
                gaze_point = get_gaze_point(row)
                if gaze_point == -1: # NaN values should be filtered, but if there's anything weird
                    print(f"NaN value for participant: {file} | File: {key}")
                
                new_row = localize_gaze(gaze_point, row, boxes) # assign gaze point to bounding box/aoi
                new_df = pd.concat([new_df, new_row], axis=1)
                
            new_df = new_df.T
            new_df.to_csv(f"{path}/{key}.csv")
            all_files[key] = new_df.to_dict('records') # dictionary to be stored as a pickle file
        pickle_dir = f"/home/zachkaras/annotated_pickle/{pid}_all.pkl"
        with open(pickle_dir, 'wb') as f:
            pickle.dump(all_files, f)

if __name__ == "__main__":
    main()
