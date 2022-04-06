import cv2
import numpy as np
  
# Reading an image
img = cv2.imread('source.jpg')
  
img = (255-img)
cv2.imshow("inverted", img)

cv2.imwrite('source_inv.jpg', img)
