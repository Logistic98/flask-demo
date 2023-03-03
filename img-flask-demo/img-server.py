# -*- coding: utf-8 -*-

from uuid import uuid1

from flask import Flask, jsonify
from flask_cors import CORS
from pre_request import pre, Rule

from code import ResponseCode, ResponseMessage
from log import logger
from utils import base64_to_img, create_date_dir

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
        "img": Rule(type=str, required=True),
        "file_name": Rule(type=str, required=False)
    }
    try:
        params = pre.parse(rule=rule)
    except Exception as e:
        logger.error(e)
        fail_response = dict(code=ResponseCode.RARAM_FAIL, msg=ResponseMessage.RARAM_FAIL, data=None)
        logger.error(fail_response)
        return jsonify(fail_response)

    # 获取参数
    image_b64 = params.get("img")
    file_name = params.get("file_name")
    if file_name is None:
        file_name = '{}.jpg'.format(uuid1())

    # 将base64字符串解析成图片保存
    img_root_path = "./img"
    img_base_path = create_date_dir(img_root_path)
    img_path = img_base_path + file_name
    try:
        base64_to_img(image_b64, img_path)
    except Exception as e:
        logger.error(e)
        fail_response = dict(code=ResponseCode.RARAM_FAIL, msg=ResponseMessage.RARAM_FAIL, data=None)
        logger.error(fail_response)
        return jsonify(fail_response)

    # 下面对保存的图片进行若干处理
    result = image_b64
    logger.info("测试日志记录")

    # 处理完成后删除生成的图片文件
    # os.remove(img_path)

    # 成功的结果返回
    success_response = dict(code=ResponseCode.SUCCESS, msg=ResponseMessage.SUCCESS, data=result)
    logger.info(success_response)
    return jsonify(success_response)


if __name__ == '__main__':
    # 解决中文乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 启动服务 指定主机和端口
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)