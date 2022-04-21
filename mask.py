import cv2
import numpy as np

# read game image
img = cv2.imread('source_hattrem.jpg', cv2.IMREAD_UNCHANGED)

# read bananas image template
template = cv2.resize(cv2.imread('hattrem.png', cv2.IMREAD_UNCHANGED), (0,0), fx=0.88, fy=0.88)
hh, ww = template.shape[:2]

# extract bananas base image and alpha channel and make alpha 3 channels
base = template[:,:,0:3]
alpha = template[:,:,3]
alpha = cv2.merge([alpha,alpha,alpha])

# do masked template matching and save correlation image
correlation = cv2.matchTemplate(img, base, cv2.TM_CCORR_NORMED, mask=alpha)

# set threshold and get all matches
threshhold = 0.95
loc = np.where(correlation >= threshhold)

print(len(loc[0]))
print(loc)
# draw matches 
result = img.copy()
for pt in zip(*loc[::-1]):
    cv2.rectangle(result, pt, (pt[0]+ww, pt[1]+hh), (0,0,255), 1)
    #print(pt)



cv2.imshow('base',base)
cv2.imshow('alpha',alpha)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
