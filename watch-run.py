import os
import subprocess
import datetime
# 录像文件名
filename = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# 存储路径
replay_path = f"/home/sam/replay"
os.makedirs(replay_path, exist_ok=True)

command = [
    "ffmpeg",
    "-f", "v4l2",
    "-video_size", "1920x1080",
    "-framerate", "30",  # 30FPS帧数
    "-i", "/dev/video0",  # 默认摄像头设备
    "-f", "alsa",
    "-i", "default",  # 默认音频设备
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-c:a", "aac",
    "-t", "180",  # 录制时长180s
    f"{replay_path}/{filename}.mp4"
]


def get_file_creation_time(replay_dir):
    """获取所有文件与文件的创建时间（Unix时间戳）"""
    file_and_createtime = []
    for root, dirs, files in os.walk(replay_dir):
        # print(files)
        for file in files:
            full_path = os.path.join(root, file)
            # print(full_path, os.path.getctime(full_path))
            file_and_createtime.append({full_path: os.path.getctime(full_path)})
    return file_and_createtime


def get_elapsed_time_since_creation(replay_path):
    """
    计算文件从创建到现在的时间差（秒）
    超过三天进行删除
    """
    for dict_data in get_file_creation_time(replay_path):
        print(dict_data)
        for key in dict_data:
            time_out = dict_data[key]
            # 现在的时间
            current_time = datetime.datetime.now().timestamp()
            elapsed_time = current_time - time_out
            if elapsed_time > 3600 * 24 * 3:  # 大于三天 删除文件
                os.remove(key)


if __name__ == '__main__':

    while True:
        # 删除老文件
        get_elapsed_time_since_creation(replay_path)
        # 录像
        subprocess.run(command, check=True)

# 6行 指定replay路径

