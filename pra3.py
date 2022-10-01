import cv2
img = cv2.imread("D:\\utra practice\\opencv practice\\uoft.jpg")
temp = cv2.resize(img, (32, 32), interpolation=cv2.INTER_LINEAR)
img_pix = cv2.resize(temp, (1140, 760), interpolation=cv2.INTER_NEAREST)
cv2.imshow("pixel art", img_pix)
cv2.waitKey(0)
if cv2.waitKey(0)=='q':
    cv2.destroyAllWindows()
    exit()