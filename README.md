## flask-demo

## 1. 项目概述

本项目是输入项为文本、图像、文件的Flask接口封装通用模板，代码讲解见：[使用Flask封装集成深度学习算法](https://www.eula.club/blogs/使用Flask封装集成深度学习算法.html)

## 2. 示例算法

### 2.1 原始构建

```
$ cd text-flask-demo
$ chmod u+x build.sh
$ ./build.sh
```

构建成功后会得到 text-flask-demo-image 镜像和 text-flask-demo 容器

### 2.2 接口文档

```
URL：http://IP:5000/api/moduleName/methodName
请求方式：POST
请求参数：body（JSON）
```

| 参数名 | 含义 | 类型   | 取值                            |
| ------ | ---- | ------ | ------------------------------- |
| type   | 类型 | int    | 1：类型一，2：类型二，3：类型三 |
| text   | 文本 | String | 任意文本                        |

### 2.3 接口测试

请求参数：

```json
{
    "type": 1,
    "text": "测试123"
}
```

返回内容：

```json
{"code":200,"data":"测试123,hello world!","msg":"请求成功"}
```

### 2.4 打包容器

可以对容器或者对镜像进行打包。

```
$ docker commit -a "demo" -m "commit text-flask-demo-image" text-flask-demo demo/text-flask-demo-image:v1.0
$ docker save -o text-flask-demo-image-v1.0.tar demo/text-flask-demo-image:v1.0
$ tar -zcvf text-flask-demo-image-v1.0.tar.gz text-flask-demo-image-v1.0.tar && rm -f text-flask-demo-image-v1.0.tar
```

然后将以下命令写成一个交付部署脚本，最终交付该镜像及交付部署脚本即可。

```
$ tar -zxvf text-flask-demo-image-v1.0.tar.gz
$ docker load -i text-flask-demo-image-v1.0.tar
$ rm -f text-flask-demo-image-v1.0.tar
$ docker run -d -p 5000:5000 --name text-flask-demo -e TZ="Asia/Shanghai" demo/text-flask-demo-image:v1.0
$ docker update text-flask-demo --restart=always
```

