import cv2 as cv

# 打开摄像头捕捉视频 函数参可以为设备的索引（设备索引就是指定哪个摄像头的数字），也可以是视频文件名字
cap = cv.VideoCapture(0)
# 定义编解码器
fourcc = cv.VideoWriter_fourcc(*'mp4v')

# 创建out视频保存对象，定义保存图像的相关参数 文件路径 编解码器 帧率 图像大小
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while cap.isOpened():
    # 获取一帧
    ret, frame = cap.read()
    # 如果摄像头开着，则ret为true
    if ret:
        # 设置图片颜色
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 将图片垂直翻转
        # frame = cv.flip(frame, 0)
        # 将读取到的每一帧数据，写入到out对象中
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(20) == ord('q'):
            break
    # else:
    #     break
# 完成工作后释放所有内容
cap.release()
out.release()
cv.destroyAllWindows()
