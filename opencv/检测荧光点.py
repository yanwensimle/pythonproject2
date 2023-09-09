import cv2
import numpy as np


def detect_fluorescent_points(image_path):
    # 读取图片
    image = cv2.imread(image_path)

    # 将图片转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用高斯滤波平滑图像
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用阈值分割图像，将荧光点区域提取出来
    _, thresholded = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

    # 寻找荧光点的轮廓
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 绘制检测到的荧光点
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # 显示结果图像
    cv2.imshow("Fluorescent Points Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 调用函数进行荧光点检测
image_path = "your_image.jpg"  # 替换为你的图片路径
detect_fluorescent_points(image_path)

# 第二种
import cv2
import numpy as np


def fluorescent_detection(image):
    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 设置荧光的颜色范围
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # 根据颜色范围创建掩膜
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 对图像和掩膜进行位运算
    fluorescent_image = cv2.bitwise_and(image, image, mask=mask)

    # 计算荧光像素的数量
    fluorescent_pixels = cv2.countNonZero(mask)

    return fluorescent_image, fluorescent_pixels


# 读取图像
image = cv2.imread("image.jpg")

# 调用荧光检测函数
fluorescent_image, fluorescent_pixels = fluorescent_detection(image)

# 显示结果
cv2.imshow("Original Image", image)
cv2.imshow("Fluorescent Image", fluorescent_image)
print("Fluorescent Pixels:", fluorescent_pixels)

cv2.waitKey(0)
cv2.destroyAllWindows()
