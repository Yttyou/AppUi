"""  视频上传至服务器处理  """

import datetime
import os
import time
import threading
from urllib.parse import urlsplit
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed
from minio import Minio
import logging
from Common import logger

minioClient = Minio(endpoint='123.57.37.36:9000', access_key='4BZ07VE7OK31MCXB3YRV',
                    secret_key='wjp5ppfRmpuSyGOAn75gsrelu15mwN8RLvberQoe', secure=False)


def create_bucket(bucket_name):
    """创建文件夹"""
    r = minioClient.bucket_exists(bucket_name)
    if r == True:
        print("文件夹已存在")
    else:
        minioClient.make_bucket(bucket_name, location="us-east-1")
        print("文件夹创建成功")


def remove_bucket(bucket_name):
    """删除文件夹"""
    r = minioClient.bucket_exists(bucket_name)
    if r == True:
        minioClient.remove_bucket(bucket_name)
        print("文件夹删除成功")
    else:
        print("文件夹不存在")

# 上传文件至服务器
def upload_file_object(bucket_name, object_name, file_path):
    """
    :param bucket_name: 服务器上存储视频的文件夹（以日期来命令）
    :param object_name: 视频文件名
    :param file_path: 视频的绝对路径
    :return: 上传视频返回对应的url元组 （可下载url、可在线打开url）
    """
    try:
        print("准备上传文件")
        start = datetime.datetime.now()
        minioClient.fput_object(bucket_name=bucket_name, object_name=object_name, file_path=file_path,
                                content_type='miniType', metadata=None)

        print("文件上传成功")
        end = datetime.datetime.now()
        wait_times = (end - start).seconds
        logging.info("本次上传视频耗时 {} s".format(wait_times))
        print("本次上传视频耗时 {} s".format(wait_times))
        download_url, file_url = get_object_url(bucket_name, object_name)
        return download_url, file_url
    except Exception as e:
        print(e)
        return "12158"

def remove_file_object(bucket_name, object_name):
    """删除文件对象"""
    minioClient.remove_object(bucket_name=bucket_name, object_name=object_name)
    print("文件删除成功")


def download_file_object(bucket_name, object_name, file_path):
    """下载文件对象"""
    minioClient.fget_object(bucket_name=bucket_name, object_name=object_name, file_path=file_path)
    print("文件下载成功")


def get_object_url(bucket_name, object_name):
    """获取文件存储路径可直接下载"""
    download_url = minioClient.presigned_get_object(bucket_name=bucket_name, object_name=object_name)
    file_url = download_url.split("?")[0]
    return download_url, file_url


def run_upload_object_file(bucket_name, object_name, file_path):
    res = upload_file_object(bucket_name, object_name, file_path)
    if res == "12158":
        for i in range(2):
            print("准备重新上传文件%s" % file_path)
            res = upload_file_object(bucket_name, object_name, file_path)
            if res != "12158":
                return res
        else:
            print("****** 重新上传次数超过限制 ******")
            return "12158"
    else:
        return res

# 删除大于30天的视频文件
def get_all_buckets():
    buckets = minioClient.list_buckets()
    for bucket_name in buckets:
        objects = minioClient.list_objects(bucket_name=bucket_name.name)
        for object_name in objects:
            file_upload_time = object_name.last_modified.strftime('%Y-%m-%d %H:%M:%S')
            timeArray = time.strptime(file_upload_time, '%Y-%m-%d %H:%M:%S')
            second = int(time.time()) - int(time.mktime(timeArray))
            if second > 30*24*60 * 60:
                remove_file_object(bucket_name.name, object_name.object_name.encode('utf-8'))


if __name__ == '__main__':
    create_bucket("56473")
    upload_file_object("56473",'180926.mp4','/Users/ytt/Documents/neptune/test_case_video_S9/180926.mp4')
    print("ttttt")