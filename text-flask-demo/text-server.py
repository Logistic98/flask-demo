# -*- coding: utf-8 -*-

import json
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from flask_docs import ApiDoc

from log import logger
from code import ResponseCode, ResponseMessage

# 创建一个服务
app = Flask(__name__)
CORS(app, supports_credentials=True)

# Flask-Doc接口文档
ApiDoc(
    app,
    title="Flask-Doc接口文档",
    version="1.0.0",
    description="Flask API Doc",
)

api = Blueprint("api", __name__)
app.config["API_DOC_MEMBER"] = ["api"]

@api.route("/api/moduleName/methodName", methods=["POST"])
def methodName():
    """方法功能说明
    @@@
    ### args
    |  args | required | request type | type |  remarks |
    |-------|----------|--------------|------|----------|
    | text |  true    |    body      | str  | 输入文本   |

    ### request
    ```json
    {"text": "xxx"}
    ```

    ### return
    ```json
    {"code": xxx, "msg": "xxx", "data": "xxx"}
    ```
    @@@
    """
    return jsonify({"code": 200, "msg": "xxx", "data": "xxx"})

app.register_blueprint(api, url_prefix="/api")


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

    # 成功的结果返回
    success_response = dict(code=ResponseCode.SUCCESS, msg=ResponseMessage.SUCCESS, data=result)
    logger.info(success_response)
    return jsonify(success_response)


if __name__ == '__main__':
    # 打印Flask-Doc接口文档路径
    print('接口文档地址：http://127.0.0.1:5000/docs/api/')
    # 解决中文乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 启动服务，指定主机和端口
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)