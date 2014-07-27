#!/usr/bin/env python
#_*_coding:utf-8_*_

import os
import shutil


'''
    读文件
'''


def read_file(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    text = ''
    for line in lines:
        text = text + line
    f.close()
    return text


'''
写文件
'''


def write_file(file_path, content, mode='w'):
    f = open(file_path, mode=mode)
    f.write(content)
    f.close()


'''
是否存在文件
'''


def is_exists_file(file_path):
    return os.path.exists(file_path)


'''
    是否是文件
'''


def is_file(file_path):
    return os.path.isfile(file_path)


'''
    是否是目录
'''


def is_dir(file_path):
    return os.path.isdir(file_path)


'''
    创建目录
'''


def mkdir(dir_path):
    if not exists(dir_path):
        os.makedirs(dir_path)


'''
    判断文件是否存在
'''


def exists(file_path):
    return os.path.exists(file_path)


'''
    备份文件
'''


def backup_file(file_path, now_day):
    if exists(file_path):
        shutil.copy(file_path, file_path + "." + now_day)


'''
    剪切文件
'''


def move(file_path, new_file_path):
    if exists(file_path):
        shutil.move(file_path, new_file_path)


'''
    浏览文件夹
'''


def list_dir(dir_path):
    if exists(dir_path) is False:
        return []
    return os.listdir(dir_path)


'''
    创建文件
'''


def create_file(file_path):
    open(file_path, "w")


def delete_file(file_path):
    return os.remove(file_path)


def get_file_create_timestamp(file_path):
    return int(os.path.getctime(file_path))


def extract_tar_all_file(file_path):
    import script

    os.system('tar xvf %s -C %s > %s 2>&1' % (file_path, script.script_dir, script.SCRIPT_TAR_LOG_FILE_PATH))


if __name__ == '__main__':
    pass