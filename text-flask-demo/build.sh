docker build -t text-flask-demo-image .
docker run -d -p 5000:5000 --name text-flask-demo -e TZ="Asia/Shanghai" text-flask-demo-image:latest
docker update text-flask-demo --restart=always