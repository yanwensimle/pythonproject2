import cv2

# 读取视频
video = cv2.VideoCapture(r"D:\img\01.mp4")
# 获取视频对象的帧数
fps = video.get(cv2.CAP_PROP_FPS)
# 设定循环条件
while video.isOpened():
    _, frame = video.read()
    cv2.imshow("video", frame)
    # 设置退出条件是输入'q'
    if cv2.waitKey(int(fps)) in [ord('q'), 27]:
        break
cv2.destroyAllWindows()
video.release()
