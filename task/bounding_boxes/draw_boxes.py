import cv2
import pandas as pd
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/home/zachkaras/.local/bin/pytesseract'

# Add code here for reading in input
img = cv2.imread('./final_stimuli/add.png')
img = img[100:1000, 10:1150]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filename = 'FIXME'

# Doing some preprocessing on the screenshot https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr/
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

img2 = img.copy()
coordinates = pd.DataFrame() # putting all coordinates for each function's bounding boxes into their own CSVs
c = 1
# adding coordinates for each word into two separate lists
for box in contours:
    
    x, y, w, h = cv2.boundingRect(box) # coordinates, width, and height
    tangle = cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0, 2)) # drawing the rectangle
    
    word_img = img2[y:y+h, x:x+w] # getting the word from the image
    word = "word{c}".format(c=c) # FIXME - temp before I can get pytesseract
    c += 1
    
    new_entry = {word: [[x, y], [x+w, y], [x, y+h], [x+w, y+h]]}
    pd.concat([coordinates, new_entry])
    
coordinates.to_csv('./word_coordinates/{file}.csv'.format(file=filename[:-4]))


