#!/usr/bin/env python3

import numpy as np
import cv2

img = cv2.imread('onnna.png', 1)

# 画像の表示
cv2.imshow('imamge', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


