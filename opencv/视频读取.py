import cv2 as cv

# 读取视频
cap = cv.VideoCapture(r"D:\img\01.mp4")

# 设定循环条件,如果能够正常读取到视频，则cap.isOpened()是true
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rgb = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)
    cv.imshow('frame', gray)
    cv.imshow('frame2', rgb)
    if cv.waitKey(75) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
