import os


def del_files(path):
    # ss_path = 'ScreenShot/'
    file_path = path
    files = os.listdir(file_path)
    for file in files:
        file_suffix = os.path.splitext(file)[1]
        if file_suffix == '.txt' or file_suffix == '.json' or file_suffix == '.csv':  # 仅删除有后缀的文件
            os.remove(file_path + file)
            # print(file)

if __name__ == '__main__':
    del_files('allure-report/xml/')
