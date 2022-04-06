import cv2 as cv
import numpy as np



source = cv.imread('source_res.jpg', cv.IMREAD_GRAYSCALE)
##source = cv.GaussianBlur(source, (3, 3), cv.BORDER_DEFAULT)

target = cv.imread('393_can.png', cv.IMREAD_UNCHANGED)

cv.imshow('source', source)
cv.imshow('target', target)

target = cv.resize(target, (0, 0), fx=0.75, fy=0.75)

result = cv.matchTemplate(source, target, cv.TM_CCOEFF_NORMED)
cv.imshow('result', result)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print(max_val)

threshold = 0.8
if max_val >= threshold:
    print("found")

else:
    print("not found")
