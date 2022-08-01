# -*- coding: utf-8 -*-

import json
from flask import Flask, jsonify, request
from flask_cors import CORS

from log import logger
from code import ResponseCode, ResponseMessage

# 创建一个服务
app = Flask(__name__)
CORS(app, supports_credentials=True)

"""
# 方法功能说明
"""
@app.route(rule='/moduleName/methodName', methods=['POST'])
def methodName():

    # 获取JSON格式的请求体，并解析
    request_data = request.get_data(as_text=True)
    request_body = json.loads(request_data)

    # 若干参数校验模块
    text = request_body.get("text")
    if not text:
        fail_response = dict(code=ResponseCode.RARAM_FAIL, msg=ResponseMessage.RARAM_FAIL, data=None)
        logger.error(fail_response)
        return jsonify(fail_response)

    # 业务处理模块
    result = "hello world!"
    logger.info("测试日志记录")

    # 成功的结果返回
    success_response = dict(code=ResponseCode.SUCCESS, msg=ResponseMessage.SUCCESS, data=result)
    logger.info(success_response)
    return jsonify(success_response)


if __name__ == '__main__':
    # 解决中文乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 启动服务，指定主机和端口
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)