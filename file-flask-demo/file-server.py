# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify, request
from flask_cors import CORS

from code import ResponseCode, ResponseMessage
from log import logger
from utils import create_date_dir


# 创建一个服务
app = Flask(__name__)
CORS(app, supports_credentials=True)

"""
# 方法功能说明
"""
@app.route(rule='/api/moduleName/methodName', methods=['POST'])
def methodName():

    # 获取参数并参数校验
    file = request.files.get('file')
    if file is None:
        fail_response = dict(code=ResponseCode.PARAM_FAIL, msg=ResponseMessage.PARAM_FAIL, data=None)
        logger.error(fail_response)
        return jsonify(fail_response)
    file_name = file.filename
    suffix = os.path.splitext(file_name)[-1]  # 获取文件扩展名

    # 校验扩展名
    suffix_list = [".avi", ".mov", ".rmvb", ".rm", ".flv", ".mp4", ".3gp", ".mpeg", ".mpg", ".dat", ".asf", ".navi", ".mkv", ".webm", ".ra", ".wmv"]
    if suffix not in suffix_list:
        fail_response = dict(code=ResponseCode.PARAM_FAIL, msg=ResponseMessage.PARAM_FAIL, data=None)
        logger.error(fail_response)
        return jsonify(fail_response)

    # 保存上传的文件
    file_root_path = "./file"
    file_base_path = create_date_dir(file_root_path)
    upload_path = file_base_path + file_name
    file.save(upload_path)

    # 下面对保存的文件进行若干处理
    result = upload_path
    logger.info("测试日志记录")

    # 处理完成后删除上传的文件
    # os.remove(upload_path)

    # 成功的结果返回
    success_response = dict(code=ResponseCode.SUCCESS, msg=ResponseMessage.SUCCESS, data=result)
    logger.info(success_response)
    return jsonify(success_response)


if __name__ == '__main__':
    # 解决中文乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 启动服务 指定主机和端口
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)