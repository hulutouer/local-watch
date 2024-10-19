# import datetime
# import time
#
# import cv2 as cv
#
# # 初始化 VideoWriter
# fourcc = cv.VideoWriter_fourcc(*'mp4v')  # 四字符代码，这里使用 MP4V 编码器
# # out = cv.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))  # 文件名，编码器，帧率，帧大小
# out = cv.VideoWriter('output.mp4', fourcc, 30.0, (1280, 720))  # 文件名，编码器，帧率，帧大小
# # 初始化相机
# cap = cv.VideoCapture(0)
# # 判断是否打开相机
# if not cap.isOpened():
#     print("无法打开相机")
#     exit()
#
# # current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
# start_time = time.time()
# while True:
#     # 逐帧捕获
#     ret, frame = cap.read()
#     # 如果正确读取帧，ret为True
#     if not ret:
#         print("无法读取数据帧")
#         break
#     out.write(frame)
#     cv.imshow('frame', frame)
#
#     if int(time.time() - start_time) >= 30:
#         break
#     # 正确退出程序
#     if cv.waitKey(1) & 0XFF == ord('q'):
#         break
#     # time.sleep(0.03)
# # 释放摄像头
# cap.release()
# # 关闭所有窗口
# cv.destroyAllWindows()
#
#
#
#
#
import cv2 as cv
import time

# 初始化摄像头
cap = cv.VideoCapture(0)

# 设置摄像头的分辨率和帧率
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv.CAP_PROP_FPS, 30)  # 尝试使用较低的帧率

# 检查设置是否成功
print("Width:", cap.get(cv.CAP_PROP_FRAME_WIDTH))
print("Height:", cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print("Frame rate:", cap.get(cv.CAP_PROP_FPS))

# 初始化 VideoWriter
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # 四字符代码，这里使用 mp4v 编码器
out = cv.VideoWriter('output.mp4', fourcc, 30.0, (1280, 720))  # 文件名，编码器，帧率，帧大小

# 判断是否打开相机
if not cap.isOpened():
    print("无法打开相机")
    exit()

start_time = time.time()

while True:
    # 逐帧捕获
    ret, frame = cap.read()

    # 如果正确读取帧，ret为True
    if not ret:
        print("无法读取数据帧")
        break

    # 检查帧尺寸
    frame_height, frame_width, _ = frame.shape
    print(f"Frame dimensions: {frame_width}x{frame_height}")

    out.write(frame)

    # 显示当前帧
    cv.imshow('frame', frame)

    if int(time.time() - start_time) >= 30:
        break

    # 正确退出程序
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有窗口
cv.destroyAllWindows()