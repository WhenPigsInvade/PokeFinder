import cv2
import numpy as np
image = cv2.imread('source_inv.jpg')

#we convert BGR image to GRAY image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplace = cv2.Laplacian(gray_image, cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))


color = cv2.cvtColor(gray_image,cv2.COLOR_GRAY2RGB)

lower = np.array([170,170,170])  #-- Lower range --
upper = np.array([255,255,255])  #-- Upper range --
mask = cv2.inRange(color, lower, upper)
res = cv2.bitwise_and(color, color, mask= mask)  #-- Contains pixels having the gray color--
cv2.imshow('Result',res)

cv2.imwrite('source_res.jpg', res)



cv2.imshow("laplacian image", laplace)
