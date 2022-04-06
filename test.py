import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('393.png', cv2.IMREAD_UNCHANGED)


gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplace = cv2.Laplacian(gray_image, cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))
cv2.imshow("laplace image", laplace)

color = cv2.cvtColor(laplace,cv2.COLOR_GRAY2RGB)
lower = np.array([170,170,170])  #-- Lower range --
upper = np.array([250,250,250])  #-- Upper range --
mask = cv2.inRange(color, lower, upper)
res = cv2.bitwise_and(color, color, mask= mask)  #-- Contains pixels having the gray color--
cv2.imshow('Result',res)


##canned = cv2.Canny(image[:,:,3], 100, 200)
##
##cv2.imshow("mask", image[:,:,3])
##
##cv2.imwrite("393_mask.png", image[:,:,3])
##
##cv2.imwrite("393_can.png", canned)
##
##
##na = cv2.imread('393_can.png')
##
### Make a True/False mask of pixels whose BGR values sum to more than zero
##alpha = np.sum(na, axis=-1) > 0
##
### Convert True/False to 0/255 and change type to "uint8" to match "na"
##alpha = np.uint8(alpha * 255)
##
### Stack new alpha layer with existing image to go from BGR to BGRA, i.e. 3 channels to 4 channels
##res = np.dstack((na, alpha))
##
### Save result
##cv2.imshow('393_result.png', res)
##


## Canny edge detection may also work
##https://pythonwife.com/edge-detection-in-opencv/#:~:text=Edge%20Detection%20in%20OpenCV%201%20Laplacian%20method%20for,Gradient%20Detection.%20...%203%20Canny%20Edge%20detection.%20?msclkid=2e6bb74cb55f11ecb8eda53e98fba497







