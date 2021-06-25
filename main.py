import cv2
import numpy as np

bear_bgr = cv2.imread('img/test.png')

# bear_bgr_blurred = cv2.blur(bear_bgr, (9, 9))
# bear_hsv_blurred = cv2.cvtColor(bear_bgr_blurred, cv2.COLOR_BGR2HSV)

bear_bgr_median = cv2.medianBlur(bear_bgr, 5)
bear_hsv_median = cv2.cvtColor(bear_bgr_median, cv2.COLOR_BGR2GRAY)
_, thr = cv2.threshold(bear_hsv_median, 100, 255, cv2.THRESH_OTSU)
# thr_adpt = cv2.adaptiveThreshold(bear_hsv_median, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 25)


# cv2.imshow('picture1',bear_bgr[:,:,0])
# cv2.imshow('pic', thr_adpt)
cv2.imshow('picture2', thr  )
cv2.waitKey(0)

# if __name__ == '__main__':
