import numpy as np
import pandas as pd
import math


#Removes entries with NaN for eye coordinates, adds fixation/saccade to the df "Type" column

def NanVelocityFilter(df,threshold,lcol):

    c= 0

    last = []
    lasttime = 0

    count = 0
    fid = 0
    dropper =[]
    saccades =[]

    for row in range(0,len(df)):
        
        data = df.loc[row, :].values.tolist()
    
        pid = data[0]
        fname = data[1]
        fid = data[2]
        timestamp = int(data[4])
        lvalid = int(data[5])
        rvalid = int(data[6])
        if rvalid == 0 or lvalid==0:
            last = [] # first valid reading after invalid cannot be classified as fixation or saccade.
            lasttime=0
            dropper.append(row)
            continue
        
        lc = data[7].replace('(','').replace(')','')
        lcs = lc.split(",")
    
        xl = float(lcs[0])
        yl = float(lcs[1])

        rc = data[8].replace('(','').replace(')','')
        rcs = rc.split(",")
        xr = float(rcs[0])
        yr = float(rcs[1])
        
        x = 1920*(xl+xr)/2
        y = 1080*(yl+yr)/2
        current = [x , y]
    
        if len(last) == 0:
            lasttime = timestamp
            last = [x , y]
            continue

        time = (timestamp-lasttime)/1000 # time difference in milliseconds, the refresh rate of the eye tracker is 120 hz every reading we have is just 8.333 ms apart

        dist = math.dist(last,current)
        velocity = dist/time # velocity in pixels/ms
    
        if velocity > threshold: #value derived from trial and error compared to 3d model, 1 here equates to about 250 pixels/s
            count += 1
            df.at[row,lcol] = 'Saccade'
            saccades.append(row)
        else:
            df.at[row,lcol] = 'Fixation'

        c += 1
        last = [x , y]
        lasttime = timestamp
    
    print(c)
    print(count)
    df.drop(dropper,axis=0,inplace=True)
    return df,fid,saccades    



if __name__ == "__main__":
    import glob
    import pickle
    path = "*writing*.csv"
    master = dict()
    pid =''
    for fname in glob.glob(path):
        pid = fname.split("_")[0]
        dframe = pd.read_csv(fname, header=None)
        lcol = len(dframe.columns)
        
        dframe[lcol] = np.nan
        df,fid,saccades = NanVelocityFilter(dframe,4,lcol)

        print(fid)    
        newdf = df.copy(deep=True)
        newdf.drop(saccades,axis=0, inplace=True)

        df.to_csv(pid+"_"+str(fid)+".csv",header=False)
        master[fid] = newdf.to_dict('index')

    print(pid)
    pickle.dump(master,open(pid+"master.pkl","wb"))
