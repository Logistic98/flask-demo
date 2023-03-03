# -*- coding: utf-8 -*-

import os
import time


# 在指定目录下创建当前日期为目录名的子目录
def create_date_dir(file_root_path):
    now_str = time.strftime("%Y%m%d", time.localtime())
    file_base_path = file_root_path + '/' + now_str + '/'
    if not os.path.exists(file_root_path):
        os.makedirs(file_root_path)
    if not os.path.exists(file_base_path):
        os.makedirs(file_base_path)
    return file_base_path
