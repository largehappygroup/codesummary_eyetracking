import difflib
import re
import os
import pandas as pd
import numpy as np

oracle = pd.read_csv('../stimuli/pruned_seeds2.csv')
box_files = os.listdir('./word_coordinates')

for boxes in box_files:
    name = re.split(string=boxes, pattern='_boxes.csv')[0]
    idx = np.where(oracle['name'] == name)[0][0]
    function = oracle['function'][idx]
    
    split_string = re.split(string=function, pattern=" |\n")
    split_string = [i for i in split_string if i]
    filename = './word_coordinates/'+boxes
    strings = pd.read_csv('./word_coordinates/'+boxes, index_col=False)
    strings.columns = ['index', 'predicted_word', 'x', 'y', 'width', 'height']
    strings = strings.drop(columns=['index'])
    new_col = pd.DataFrame()
    
    for word in strings['predicted_word']:
        try:
            closest_matches = difflib.get_close_matches(word, split_string, n=3)
            new_col = pd.concat([new_col, pd.Series(closest_matches[0])], ignore_index=True)
        except:
            new_col = pd.concat([new_col, pd.Series('-----------')], ignore_index=True)
    strings['word'] = new_col #.insert(loc=0, column='word', value=new_col)
    strings = strings[['word', 'predicted_word', 'x', 'y', 'width', 'height']]
    strings.to_csv(('./word_coordinates/'+boxes), index=False, header=True)


