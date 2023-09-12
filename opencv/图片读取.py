import cv2

# 读取图像，第一种是正常读取，第二种是读取灰度图像
img = cv2.imread(r"D:\img\02.jpg")
gray = cv2.imread(r"D:\img\02.jpg", 0)
# 显示图像也同样
cv2.imshow("colorful", img)
cv2.imshow("gray", gray)
# 不再等待键盘输入事件，直接显示
cv2.waitKey(0)
# 关闭所有显示窗口
cv2.destroyAllWindows()

