import cv2 as cv

# 打开摄像头
cap = cv.VideoCapture(0)
# 定义编解码器并创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# 提取录制的视频图像大小，与保存的图像参数要相符
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# 定义保存图像的相关参数 文件路径 编解码器 帧率 图像大小
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while True:
    # 获取一帧
    ret, frame = cap.read()
    # 如果摄像头开着，则ret为true
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # frame = cv.flip(frame, 0)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(20) == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()
