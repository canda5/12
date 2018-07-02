# -*- coding: utf-8 -*-

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while(1):
 
    # フレームを取得
    ret, frame = cap.read()
 
    # フレームをHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # 取得する色の範囲を指定する
    lower_yellow = np.array([20, 50, 50])
    upper_yellow = np.array([60, 255, 255])
    
    lower_red = np.array([120, 50, 50])
    upper_red = np.array([180, 255, 255])

    lower_blue = np.array([60, 50, 50])
    upper_blue = np.array([120, 255, 255])
    # 指定した色に基づいたマスク画像の生成
    img_masky = cv2.inRange(hsv, lower_yellow, upper_yellow)
    img_maskr = cv2.inRange(hsv, lower_red, upper_red)
    img_maskb = cv2.inRange(hsv, lower_blue, upper_blue)
    # フレーム画像とマスク画像の共通の領域を抽出する。
    img_colory = cv2.bitwise_and(frame, frame, mask=img_masky)
    img_colorr = cv2.bitwise_and(frame, frame, mask=img_maskr)
    img_colorb = cv2.bitwise_and(frame, frame, mask=img_maskb)
    cv2.imshow("SHOW YELLOW IMAGE", img_colory)
    cv2.imshow("SHOW RED IMAGE", img_colorr)
    cv2.imshow("SHOW BLUE IMAGE", img_colorb)
    cv2.imshow("SHOW RGB", frame)
    # qを押したら終了
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()