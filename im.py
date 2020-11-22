import cv2
import numpy as np
img = cv2.imread("carpet.jpg")
averaging = cv2.blur(img, (21,21))
gaussian = cv2.GaussianBlur(img,(21,21),0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 5, 75, 75)
cv2.imshow("Original image", img)
cv2.imshow("Averaging", averaging)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyAllWindows()