# -*- coding: utf-8 -*-

import requests


def file_flask_test():
    # 测试请求
    url = 'http://{0}:{1}/api/moduleName/methodName'.format("127.0.0.1", "5000")
    # post传递数据
    file_path = './test_file/test.mp4'
    files = {'file': open(file_path, "rb")}
    r = requests.post(url, files=files)
    print(r.text)


if __name__ == '__main__':
    file_flask_test()
