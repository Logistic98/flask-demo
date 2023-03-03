docker build -t file-flask-demo-image .
docker run -d -p 5000:5000 --name file-flask-demo -e TZ="Asia/Shanghai" file-flask-demo-image:latest
docker update file-flask-demo --restart=always