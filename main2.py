# 그냥 새로 만듦

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\COM\Downloads\python\picture.jpg")
img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, d = 9, sigmaColor = 250, sigmaSpace = 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)

cv2.imshow('Cartoon', cartoon)
cv2.imwrite('cartoon_result.jpg', cartoon)
cv2.waitKey(0)
cv2.destoryAllWindows()