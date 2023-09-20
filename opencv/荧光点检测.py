import cv2
import numpy as np

# 加载图像
image = cv2.imread('04.jpg')
# 将图像转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义荧光的颜色范围
lower_green = np.array([85, 80, 73])
upper_green = np.array([107, 255, 255])

# 根据颜色范围创建掩膜
mask = cv2.inRange(hsv, lower_green, upper_green)

# 执行形态学操作以去除噪声
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(6,6))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(18,18))
# open先腐蚀后膨胀，去除小白点
# close先膨胀后腐蚀，去除小黑点
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel2)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel1)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel2)
# dst = cv2.GaussianBlur(mask, (5, 5), 15)
# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, dst)
# 在原始图像上绘制荧光位置
result = cv2.bitwise_and(image, image, mask=mask)

# # 寻找荧光点的轮廓
# contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # 绘制检测到的荧光点
# cv2.drawContours(image, contours, -1, (0, 255, 0), -1)
# 显示结果图像
cv2.namedWindow('Fluorescent Detection', 0)
# cv2.imshow("Fluorescent Detection", image)
cv2.imshow('Fluorescent Detection', result)

# cv2.imwrite('06.png', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
