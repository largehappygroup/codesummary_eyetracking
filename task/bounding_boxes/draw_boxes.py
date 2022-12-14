import cv2

img = cv2.imread('337.jpg')
img = img[90:1000, 25:950]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))

dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(contours)

img2 = img.copy()

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    
    rect = cv2.rectangle(img2, (x, y), (x +w, y + h), (0, 255, 0), 2)
    
cv2.imwrite("./test.jpg", img2)


# draw boxes
# recognize word in that region --> pytesseract
# hash table of words in code for each stimulus
# screenshot every time someone makes a keystroke? Or a space?
