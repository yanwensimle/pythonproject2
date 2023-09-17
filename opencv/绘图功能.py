import cv2
import numpy as np

# 创建一张空白的画布
canvas = np.zeros((500, 500, 3), dtype=np.uint8)
# 在画布上绘制一条线段
start_point = (100, 100)
end_point = (400, 400)
color = (0, 0, 255)  # 红色线段
thickness = 3
cv2.line(canvas, start_point, end_point, color, thickness)

# 在画布上绘制一个矩形
top_left = (200, 200)
bottom_right = (400, 400)
color = (0, 255, 0)  # 绿色矩形
thickness = 2
cv2.rectangle(canvas, top_left, bottom_right, color, thickness)

# 在画布上绘制一个圆形
center = (300, 300)
radius = 100
color = (255, 0, 0)  # 蓝色圆形
thickness = -1  # 填充圆形
cv2.circle(canvas, center, radius, color, thickness)

# 在画布上绘制一个椭圆
center = (250, 250)
axes = (150, 100)
angle = 0
start_angle = 0
end_angle = 360
color = (0, 255, 255)  # 黄色椭圆
thickness = 2
cv2.ellipse(canvas, center, axes, angle, start_angle, end_angle, color, thickness)

# 在画布上绘制一个多边形
points = np.array([[100, 100], [200, 50], [300, 150], [250, 200]], np.int32)
points = points.reshape((-1, 1, 2))
color = (255, 255, 0)  # 青色多边形
thickness = 2
cv2.polylines(canvas, [points], True, color, thickness)

# 在画布上绘制文本
text = 'OpenCV'
position = (200, 250)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
color = (255, 255, 255)  # 白色文本
thickness = 2
cv2.putText(canvas, text, position, font, font_scale, color, thickness)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
