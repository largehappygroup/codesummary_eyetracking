import cv2

img = cv2.imread('./final_stimuli/add.png')
img = img[100:1000, 10:1150]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# adding coordinates for each word into two separate lists
# then finding mins and maxes 
for box in contours:
    x_coord = []
    y_coord = []
    for coord in box:
        for pair in coord:
            x_coord.append(pair[0])
            y_coord.append(pair[1])
            
    print(x_coord)
    exit(1)
    



img2 = img.copy()

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    
    rect = cv2.rectangle(img2, (x, y), (x +w, y + h), (0, 255, 0), 2)
    
#cv2.imwrite("./test_add.jpg", img2)


# draw boxes
# recognize word in that region --> pytesseract
# hash table of words in code for each stimulus
# screenshot every time someone makes a keystroke? Or a space?
