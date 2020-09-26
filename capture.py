import cv2
import os

read = cv2.imread('img/image1.png')

cv2.imshow("test", read)
cv2.waitKey(0)
cv2.destroyAllWindows()