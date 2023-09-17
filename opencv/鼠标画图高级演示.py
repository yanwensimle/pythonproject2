import numpy as np
import cv2

# 鼠标按下为true,可以进行画画图
drawing = False
# mode = True
ix, iy = -1, -1


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global drawing, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # 鼠标按下，记下鼠标起始的坐标
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if (drawing == True):
            #     if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
            # else:
            #     cv2.circle(img, (x, y), 50, (0, 255, 0), 3)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


# 创建一个黑色的图像，一个窗口
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('opencv')
# 将回调函数绑定到指定窗口下，第一个参数为窗口名称，第二个参数为回调函数
cv2.setMouseCallback('opencv', draw_circle)
# 不停的刷新窗口显示的内容
while 1:
    cv2.imshow('opencv', img)
    if cv2.waitKey(10) & 0xFF == 27:
        break
    # elif cv2.waitKey(1) & 0xFF == ord('m'):
    #     mode = not mode
cv2.imwrite('01.jpg', img)
cv2.destroyAllWindows()
