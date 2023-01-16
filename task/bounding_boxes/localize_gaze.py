import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon

# df = pd.read_csv(csv_dir + csv_file)
# df.columns = ["pid", "function_name", "function_id", "system_timestamp", "device_timestamp", "valid_gaze_left",
#               "valid_gaze_right", "gaze_left", "gaze_right", "valid_pd_left", "valid_pd_right", "pd_left", "pd_right"]

# dflen = len(df)
# df_valid = df[(df['valid_gaze_left'] == 1)]
# df_valid = df[(df['valid_gaze_right'] == 1)]
# df_valid = df[(df['valid_pd_right'] == 1)]
# df_valid = df[(df['valid_pd_left'] == 1)]

# img_path = os.getcwd() + '/' + framelist[0]
# img = cv2.imread(img_path)
# dimensions = img.shape

# # height, width, number of channels in image
# height = img.shape[0]
# width = img.shape[1]

# def return_x_y(gaze):
#     pattern = "[()]"
#     new_gaze_string = re.sub(pattern, "", gaze)

#     xyz = new_gaze_string.split(',')
#     if xyz[0] == 'nan' or xyz[1] == 'nan':
#         return "oof", "oof"

#     x = round(width*float(xyz[0]))
#     y = round(height*float(xyz[1]))

#     return x, y

#for box in contours:
#    new_tangle = pd.Series(
#        {word: Polygon([(x, y), (x+w, y), (x, y+h), (x+w, y+h)])})
#    boxes = pd.concat([boxes, new_tangle])

# points = [Point(15, 500), Point(237, 258), Point(135, 300)]
# pnts = geopandas.GeoDataFrame(geometry=points, index=['A', 'B', 'C'])
# pnts = pnts.assign(**{key: pnts.within(geom) for key, geom in boxes.items()})

# df = pd.DataFrame(pnts)
# df.to_csv('./localizingTest.csv')


### Steps ###
# With eyetracking data
# 1. Read in gaze file into pd dataframe
# 2. convert and average the L/R gaze coordinates
# 3. Read in matching coordinate file 
# 4. Make all coordinates into geopandas points
# 5. Loop through gaze file to see if points localize 
# 6. Add columns to pd Dataframes then write as csv files



