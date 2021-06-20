#!/usr/bin/env python3

import numpy as np
from scipy import linalg
 
A = np.array([[1,3,2],[-1,0,1],[2,3,0]])
 
AI = linalg.inv(A)
 
print(AI)
