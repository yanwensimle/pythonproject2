import cv2

video = cv2.VideoCapture(0)
while True:
    # 获取一帧
    _, frame = video.read()
    # 将这帧转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(0) == ord('q'):
        break

video.release()
