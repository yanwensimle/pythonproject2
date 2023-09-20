import cv2 as cv
import numpy as np
# 读取图像，第一种是正常读取，第二种是读取灰度图像
# 通过imread函数读取图片信息,第一个参数为图片地址，第二个参数为图像格式：1为彩色是默认值，0为灰色，-1包括alpha通道
img = cv.imread(r"02.png")
gray = cv.imread(r"02.png", 0)
# cv.namedWindow('image', cv.WINDOW_NORMAL)
# 显示图像，第一个参数为文件名，第二个参数为要显示的数据
cv.imshow("colorful", img)
cv.imshow("gray", gray)
# 不再等待键盘输入事件，直接显示
k = cv.waitKey(0)
if k == 27:  # ESC 退出
    cv.destroyAllWindows()
elif k == ord('s'):  # 's' 保存退出
    cv.imwrite('03.png', gray)
    cv.destroyAllWindows()
# 关闭所有显示窗口
