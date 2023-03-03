import os
import cv2
import numpy as np
import pandas as pd
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import pytesseract
import keras_ocr

#pytesseract.pytesseract.tesseract_cmd = '/home/zachkaras/.local/bin/pytesseract'

# Add code here for reading in input


img = cv2.imread('./final_stimuli/add.png')
img = img[100:1000, 10:1150]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
print(gray.shape)
filename = 'FIXME'
pipeline = keras_ocr.pipeline.Pipeline()
test = keras_ocr.tools.read(gray)
test = pipeline.recognize(gray)
print(gray)
exit(1)

# Doing some preprocessing on the screenshot https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

img2 = img.copy()

# coordinates = pd.DataFrame() # putting all coordinates for each function's bounding boxes into their own CSVs
# c = 1
# test = []
# kernel = np.array([[0, -1, 0],
#                    [-1, 5,-1],
#                    [0, -1, 0]])
# #kernel = np.ones((5, 5), np.uint8)

# adding coordinates for each word into two separate lists
for box in contours:
    
    x, y, w, h = cv2.boundingRect(box) # coordinates, width, and height
    tangle = cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0, 2)) # drawing the rectangle
    
    word_img = img2[y+1:(y+1)+(h-1), x+1:(x+1)+(w-1)] # getting the word from the image
    word_x = word_img.shape[1]
    word_y = word_img.shape[0]
    word_img2 = cv2.resize(word_img, (word_x * 4, word_y * 4))
    
    gray2 = cv2.cvtColor(word_img2, cv2.COLOR_BGR2GRAY)
    #gray2 = cv2.dilate(gray2, kernel, iterations=1)
    #gray2 = cv2.erode(gray2, kernel=kernel, iterations=2)
    sharp = cv2.filter2D(src=gray2, ddepth=-1, kernel=kernel)
    blur = cv2.bilateralFilter(sharp, 9, 75, 75)
    
    ret1, thresh1 = cv2.threshold(blur, 180, 255, cv2.THRESH_BINARY)
    #word_img2 = cv2.GaussianBlur(gray2, (5, 5), 0)
    
    cv2.imwrite("./temp/{c}.png".format(c=c), thresh1)
    #cv2.imwrite("./temp/{c}.png".format(c=c), thresh1)
    #word = "word{c}".format(c=c)
    word = pytesseract.image_to_string(thresh1)

    test.append(word)
    c += 1
    
    #new_entry = {word: [[x, y], [x+w, y], [x, y+h], [x+w, y+h]]}
    #pd.concat([coordinates, new_entry])
    
#coordinates.to_csv('./word_coordinates/{file}.csv'.format(file=filename[:-4]))
print(test)
print(len(test))

