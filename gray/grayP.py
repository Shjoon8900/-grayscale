import cv2
import numpy as np
import matplotlib.pyplot as plt 

image = cv2.imread("people.jpg")
#print(image.shape)


gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

cv2.imwrite('people.jpg',gray)

cv2.imshow('people.jpg',gray)
I = cv2.waitKey(0)

if I == 27 or I == ord('s'):
    cv2.destoryAlWindows()
