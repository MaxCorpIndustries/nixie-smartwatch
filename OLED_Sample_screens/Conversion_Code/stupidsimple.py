from PIL import Image
import numpy as np
#"frames_animate_test/frame0.png"
import cv2

import os
import sys
import binascii

path = "frames_animate_test/frame0.png"

image_file = Image.open(path) 
bilevel_img = image_file.convert('1')
data_array = np.array(bilevel_img)
print(data_array)
