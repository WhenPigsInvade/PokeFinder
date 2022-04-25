import numpy as np
import cv2
import os
import time

# read game image
img = cv2.imread('source_yamper.jpg')
img = cv2.resize(img, (0,0), fx=0.2, fy=0.2)

start = time.time()

path_of_the_directory= 'Pictures'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):

        min_loc = 0
        threshhold = 0.96

        picture = cv2.imread(f, cv2.IMREAD_UNCHANGED)
        for size in np.linspace(0.13, 0.18, 11):
            # read bananas image template
            template = cv2.resize(picture, (0,0), fx=size, fy=size)
            hh, ww = template.shape[:2]

            # extract bananas base image and alpha channel and make alpha 3 channels
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            # do masked template matching and save correlation image
            correlation = cv2.matchTemplate(img, base, cv2.TM_CCORR_NORMED, mask=alpha)

            # set threshold and get all matches
            loc = np.where(correlation >= threshhold)



            # found the best fit
            if len(loc[0]) != 0 and len(loc[0]) < 200:
                print(filename)
                print(len(loc[0]))
                print(size)


        #Now flipped
        picture = cv2.flip(picture, 1)
        for size in np.linspace(0.13, 0.18, 11):
            # read bananas image template
            template = cv2.resize(picture, (0,0), fx=size, fy=size)
            hh, ww = template.shape[:2]

            # extract bananas base image and alpha channel and make alpha 3 channels
            base = template[:,:,0:3]
            alpha = template[:,:,3]
            alpha = cv2.merge([alpha,alpha,alpha])

            # do masked template matching and save correlation image
            correlation = cv2.matchTemplate(img, base, cv2.TM_CCORR_NORMED, mask=alpha)

            # set threshold and get all matches
            loc = np.where(correlation >= threshhold)



            # found the best fit
            if len(loc[0]) != 0 and len(loc[0]) < 200:
                print(filename)
                print(len(loc[0]))
                print(size)
                print('flipped')



print(time.time() - start)
