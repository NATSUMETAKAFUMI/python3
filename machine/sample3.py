#!/usr/bin/env python3

import cv2

img = cv2.imread('onnna.png')

img = cv2.rectangle(img, (250, 300), (350, 250), (0, 0, 0), -1)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
