import numpy as np
import cv2

img = cv2.imread('home.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp,dec = sift.detectAndCompute(gray,None)
img=cv2.drawKeypoints(gray,kp,img)
cv2.imwrite('sift_keypoints.jpg',img)
#img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.imwrite('sift_keypoints_2.jpg',img)

print(np.shape(dec))

#sift = cv2.SIFT_create()

#keypoints, descriptors = sift.detectAndCompute(img, None)
