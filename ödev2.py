#Hilem Nur Erdem 02215076005

import cv2
import numpy as np

image = cv2.imread('path/to/your/image.jpg')

#RBG formatından HSV ye dönüştürme
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Kırmızı renk için
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)

#Kırmızılar kapıl diğerleri gözükmeyecek şekilde ayarlama
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Original', image)
cv2.imshow('Red Only', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
