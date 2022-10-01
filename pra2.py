import cv2
img = cv2.imread("D:\\utra practice\\opencv practice\\uoft.jpg")
img_b = img[:,:,0]
img_g = img[:,:,1]
img_r = img[:,:,2]
# img_b, img_g, img_r = cv2.split(img)
cv2.imshow("img_b", img_b)
cv2.imshow("img_g", img_g)
cv2.imshow("img_r", img_r)
cv2.waitKey(0)
if cv2.waitKey(0)=='q':
    cv2.destroyAllWindows()
    exit()
