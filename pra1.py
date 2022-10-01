import cv2
img = cv2.imread("D:\\utra practice\\opencv practice\\uoft.jpg")
img_re = cv2.resize(img, (200, 100))
cv2.imshow("uoft", img_re)
cv2.waitKey(0)
if cv2.waitKey(0) == 'q':
    cv2.destroyAllWindows()