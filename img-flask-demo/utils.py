# -*- coding: utf-8 -*-

import base64

# 解析base64生成图像文件
def base64_to_img(image_b64, img_path):
    imgdata = base64.b64decode(image_b64)
    file = open(img_path, 'wb')
    file.write(imgdata)
    file.close()
