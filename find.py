import numpy as np
import cv2
import os
import time

## Default threshhold = 0.97
def find(filename, threshhold):
    results = {}
    # read game image
    img = cv2.imread(filename)
    img = cv2.resize(img, (0,0), fx=0.20, fy=0.20)

    start = time.time()

    path_of_the_directory= 'Pictures'
    for filename in os.listdir(path_of_the_directory):
        f = os.path.join(path_of_the_directory,filename)
        if os.path.isfile(f):

            min_loc = 0

            picture = cv2.imread(f, cv2.IMREAD_UNCHANGED)
            for size in np.linspace(0.10, 0.19, 25):
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
                    if filename in results.keys():
                        results.update({filename:results[filename]+1})
                    else:
                        results.update({filename:1})

                template = cv2.flip(template, 1)
                base = cv2.flip(base, 1)
                alpha = cv2.flip(alpha, 1)
                
                correlation = cv2.matchTemplate(img, base, cv2.TM_CCORR_NORMED, mask=alpha)

                # set threshold and get all matches
                loc = np.where(correlation >= threshhold)



                # found the best fit
                if len(loc[0]) != 0 and len(loc[0]) < 200:
                    if filename in results.keys():
                        results.update({filename:results[filename]+1})
                    else:
                        results.update({filename:1})



    print(sorted(results.items(), key =lambda kv:(kv[1], kv[0])))
    print(time.time() - start)

