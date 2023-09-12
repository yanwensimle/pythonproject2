import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'D:\img\02.jpg', 1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度值
plt.show()
