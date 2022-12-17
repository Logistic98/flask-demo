docker build -t img-flask-demo-image .
docker run -d -p 5000:5000 --name img-flask-demo -e TZ="Asia/Shanghai" img-flask-demo-image:latest
docker update img-flask-demo --restart=always