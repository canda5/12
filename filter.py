# -*- coding: utf-8 -*-
import numpy as np

import cv2

from matplotlib import pyplot as plt


def myfunc(i):

    pass # do nothing



cv2.namedWindow('filter') # create win with win name



cv2.createTrackbar('value', # name of value

                   'filter', # win name

                   0, # min

                   100, # max

                   myfunc) # callback func





cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)





while(True):



    ret, frame = cap.read()

    if not ret: continue





    v = cv2.getTrackbarPos('value',  # get the value

                           'filter')  # of the win



    ## do something by using v

    if v!=0:

        kernel = np.ones((v,v),np.float32)/(v**2)

        frame2 = cv2.filter2D(frame,-1,kernel)

    else:

        kernel = np.ones((1,1),np.float32)

        frame2 = cv2.filter2D(frame,-1,kernel)



    cv2.imshow('filter', frame2)  # show in the win



    k = cv2.waitKey(1)

    if k == ord('q') or k == 27:

        break







cap.release()

cv2.destroyAllWindows()