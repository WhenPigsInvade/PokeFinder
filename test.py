import numpy as np
import cv2
import os
import time

# read game image
img = cv2.imread('source.jpg')

start = time.time()

path_of_the_directory= 'Pictures'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):

        min_loc = 0
        for size in np.linspace(0.65, 0.85, 5):
            # read bananas image template
            template = cv2.resize(cv2.imread(f, cv2.IMREAD_UNCHANGED), (0,0), fx=size, fy=size)
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



            # found the best fit
            if len(loc[0]) != 0 and len(loc[0]) < 200 and len(loc[0]) > min_loc:
                print(filename)
                print(len(loc[0]))
                print(size - 0.01)
                break
            elif len(loc[0]) != 0:
##                print(len(loc[0]))
                min_loc = len(loc[0])

    ##            result = img.copy()
    ##            for pt in zip(*loc[::-1]):
    ##                cv2.rectangle(result, pt, (pt[0]+ww, pt[1]+hh), (0,0,255), 1)
    ##            cv2.imshow('result',result)
    ##            cv2.waitKey(0)
    ##            cv2.destroyAllWindows()

print(time.time() - start)
