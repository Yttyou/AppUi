import os

def sizeConvert(size):  # 单位换算
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(int(size / G)) + 'G'
    elif size >= M:
        return str(int(size / M)) + 'M'
    elif size >= K:
        return str(int(size / K)) + 'K'
    else:
        return str(size) + 'Bytes'

def get_filesize(filename):
    u"""
    获取文件大小（M: 兆）
    """
    file_byte = os.path.getsize(filename)
    return sizeConvert(file_byte)

# 通过文件大小，给与指定时间
def get_video_ou_gif_time(filename):
    data = get_filesize(filename)   # 文件大小
    print(data)
    if data.find("M") >0:
        video_size = int(data.split("M")[0])
        if video_size <= 30:
            return 6
        elif 30< video_size <= 50:
            return 10
        elif 50< video_size <= 70:
            return 15
        elif 70< video_size <= 90:
            return 18
        elif 90< video_size <= 120:
            return 24
        elif video_size>120:
            return 30
    else:
        return 5

def sadsdas():
    mac_video_path = "/Users/ytt/Desktop/yyy.mp4"
    gif_mac_path = "/Users/ytt/Desktop/yyy.gif"
    os.popen("ffmpeg -i {0} -s 720x1440 -b:v 700k {1}".format(mac_video_path, gif_mac_path))


if __name__ == '__main__':
    print(type(get_video_ou_gif_time('/Users/ytt/Downloads/4kvideodownloader_4.12.1.msi')))
    # sadsdas()
    # print("hahah ")