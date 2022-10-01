import cv2
import numpy as np
img = cv2.imread("D:\\utra practice\\opencv practice\\sunrise.jpg")
orange = (0, 165, 255)
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if img[i, j, 0]<=orange[0]+70 and orange[1]-70<=img[i, j, 1]<=orange[1]+50 and orange[2]-70<=img[i, j, 2]:
            continue
        else:
            img[i, j, 0] = 0
            img[i, j, 1] = 0
            img[i, j, 2] = 0
cv2.imshow("orange_pic", img)
cv2.waitKey(0)
if cv2.waitKey(0)=='q':
    cv2.destroyAllWindows()
    exit()