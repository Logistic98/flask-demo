# -*- coding: utf-8 -*-

import base64
import json
import requests


def img_flask_test():
    # 测试请求
    url = 'http://{0}:{1}/api/moduleName/methodName'.format("127.0.0.1", "5000")
    f = open('./test_img/test.png', 'rb')
    # base64编码
    base64_data = base64.b64encode(f.read())
    f.close()
    base64_data = base64_data.decode()
    # 传输的数据格式
    data = {'img': base64_data, 'file_name': '测试中文.png'}
    # post传递数据
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(r.text)


if __name__ == '__main__':
    img_flask_test()
