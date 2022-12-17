# -*- coding: utf-8 -*-


import requests


def text_flask_test():
    # 测试请求
    url = 'http://{0}:{1}/api/moduleName/methodName'.format("127.0.0.1", "5000")
    # 传输的数据格式
    data = {'text': "测试123", 'type': 1}
    # post传递数据
    r = requests.post(url, data=data)
    print(r.text)


if __name__ == '__main__':
    text_flask_test()

