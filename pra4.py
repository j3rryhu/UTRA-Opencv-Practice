import cv2
import numpy as np
sunrise = cv2.imread("sunrise.jpg")
sunrise = cv2.cvtColor(sunrise, cv2.COLOR_BGR2RGB)
pixel_val = sunrise.reshape((-1, 3))
pixel_val = np.float32(pixel_val)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 5
attempts = 10
_, labels, centers = cv2.kmeans(pixel_val, K, None, criteria, attempts, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
# new_center = [centers[0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]
# new_center = np.uint8(new_center)
x_coord = []
y_coord = []
reshaped_labels = labels.flatten().reshape(sunrise.shape[:2])
print(reshaped_labels)
for j in range(0, sunrise.shape[0]):
    for i in range(0, sunrise.shape[1]):
        if reshaped_labels[j][i] == 0 and reshaped_labels[j+1][i]==0:
            y_coord.append(j)
            x_coord.append(i)
center_x = int((max(x_coord)+min(x_coord))/2)
center_y = int((max(y_coord)+min(y_coord))/2)
segmented_img = centers[labels.flatten()]
result = segmented_img.reshape(sunrise.shape)
center_y-=30
cv2.circle(result, (center_x, center_y), 10, (255, 0, 0))
cv2.imshow("segmented img", result)
cv2.waitKey(0)
if cv2.waitKey(0)=='q':
    cv2.destroyAllWindows()
    exit()
