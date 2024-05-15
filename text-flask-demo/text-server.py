# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
from pre_request import pre, Rule

from log import logger
from code import ResponseCode, ResponseMessage

# 创建一个服务
app = Flask(__name__)
CORS(app, supports_credentials=True)

"""
# 方法功能说明
"""
@app.route(rule='/api/moduleName/methodName', methods=['POST'])
def methodName():

    # 参数校验
    rule = {
        "text": Rule(type=str, required=True, gte=3, lte=255),
        "type": Rule(type=int, required=True, gte=1, lte=1)
    }
    try:
        params = pre.parse(rule=rule)
    except Exception as e:
        logger.error(e)
        fail_response = dict(code=ResponseCode.PARAM_FAIL, msg=ResponseMessage.PARAM_FAIL, data=None)
        logger.error(fail_response)
        return jsonify(fail_response)

    # 获取参数
    text = params.get("text")

    # 业务处理模块
    result = text + ",hello world!"
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