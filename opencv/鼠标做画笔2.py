import numpy as np
import cv2 as cv


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


# 创建一个黑色的图像，一个窗口
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
# 图像框图与鼠标回调函数绑定
cv.setMouseCallback('image', draw_circle)
# 进入循环，不停的刷新显示图像，按esc跳出循环
while 1:
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
