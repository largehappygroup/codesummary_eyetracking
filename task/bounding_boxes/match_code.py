import difflib
import re
import os
import pandas as pd

oracle = pd.read_csv('../stimuli/pruned_seeds2.csv')
strings = pd.read_csv('./setSecurityMode_boxes.csv')


curr = oracle['function'][0]
split_string = re.split(string=curr, pattern=" |\n")
split_string = [i for i in split_string if i]
print(split_string)

#large_string = 'the quick brown fox jumps over the lazy dog'
#split_string = re.split(pattern=" ", string=large_string)
# A string to compare to the large string
#string_to_compare = 'thee'

for word in strings['word']:
    #print(word)
    closest_matches = difflib.get_close_matches(word, split_string, n=3)
    try:
        print(word, closest_matches[0])
    except:
        print('-------------------')
        

# Print the closest match
#print(closest_matches[0])

# Use regex to split string based on splits done by OCR for bounding boxes. 
# by spaces, not by periods. 

