---
layout: post
title: Elastic Beanstalk Multicontainers + Docker + Nginx + Gunicorn + Django + Postgres
published: true
---

This is a guide on how to deploy a multicontainer Docker web application on Amazon Elastic Beanstalk. The web application will be a basic Django hello world, but has a completely functioning Postgres database. This post is geared towards beginners. 

# Motivation
Learning web development is challenging, and a lot of it is just trying out what works. But it helps to understand the big picture. 

# The Big Picture
```
Web Client <=> Elastic Beanstalk Load Balancer <=> Nginx <=> Gunicorn <=> uWSGI <=> Django
```

Install Docker

Set up the project directory.
```
mkdir myproject
cd myproject
```

Create a virtual environment, and activate. 

```
python3 -m venv .venv
source .venv/bin/activate
```

Create requirements.txt:

```
Django==2.0.7
gunicorn==19.6.0
psycopg2==2.7.5
```

```
django-admin.py startproject myproject app
```

In app/myproject/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

```
ALLOWED_HOSTS = ['app']
```

```
pip install docker-compose
```

config/app/Dockerfile

```
# Creating image based on official python3 image
FROM python:3

# Your contacts, so people blame you afterwards
MAINTAINER Pavel Gasanov <pogasanov@gmail.com>

# Sets dumping log messages directly to stream instead of buffering
ENV PYTHONUNBUFFERED 1

# Creating and putting configurations
RUN mkdir /config
ADD config/app /config/

# Installing all python dependencies
RUN pip install -r /config/requirements.txt

# Open port 8000 to outside world
EXPOSE 8000

# When container starts, this script will be executed.
# Note that it is NOT executed during building
CMD ["sh", "/config/on-container-start.sh"]

# Creating and putting application inside container
# and setting it to working directory (meaning it is going to be default)
RUN mkdir /app
WORKDIR /app
ADD app /app/
```

config/app/on-container-start.sh

```
# Create migrations based on django models
python manage.py makemigrations

# Migrate created migrations to database
python manage.py migrate

# Start gunicorn server at port 8000 and keep an eye for app code changes
# If changes occur, kill worker and start a new one
gunicorn --reload myproject.wsgi:application -b 0.0.0.0:8000
```

config/nginx/app.conf
```
# define group app
upstream app {
  # balancing by ip
  ip_hash;

  # define server app
  server app:8000;
}

# portal
server {
  # all requests proxies to app
  location / {
        proxy_pass http://app/;
    }

  # only respond to port 8000
  listen 8000;

  # domain localhost
  server_name localhost;
}
```

docker-compose.yml

```
# File structure version
version: '3'

services:
  # Database based on official postgres image
  db:
    image: postgres
    hostname: db

  # Our django application
  # Build from remote dockerfile
  # Connect local app folder with image folder, so changes will be pushed to image instantly
  # Open port 8000
  app:
    build:
      context: .
      dockerfile: config/app/Dockerfile
    hostname: app
    volumes:
      - ./app:/app
    expose:
      - "8000"
    depends_on:
      - db

  # Web server based on official nginx image
  # Connect external 8000 (which you can access from browser)
  # with internal port 8000(which will be linked to app port 8000 in configs)
  # Connect local nginx configuration with image configuration
  nginx:
    image: nginx
    hostname: nginx
    ports:
      - "8000:8000"
    volumes:
      - ./config/nginx:/etc/nginx/conf.d
    depends_on:
      - app
```

Then you can do docker-compose up
```
docker build -t raymondhfeng/myproject -f config/app/Dockerfile .
docker login
docker push raymondhfeng/myproject
```

```
pip install awsebcli
```
Dockerrun.aws.json
```
{
 "AWSEBDockerrunVersion": "1",
 "Image": {
   "Name": "pogasanov/myproject:latest",
   "Update": "true"
 },
 "Ports": [
   {
     "ContainerPort": "8000"
   }
 ]
}
```

will need iam with these permissions

AmazonS3FullAccess
AWSCodeDeployFullAccess
AWSElasticBeanstalkFullAccess
AWSCodeDeployRole
AWSElasticBeanstalkService

AWSElasticBeanstalkMultiContainer

```
eb init
eb create
```

be careful, dont lose track of your usage of amazon ec2 instances

# References:
- https://github.com/micahhausler/container-transform
- https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/single-container-docker-configuration.html
- https://pogasanov.ru/posts/django-docker-aws
	- https://github.com/pogasanov/django-docker-aws
- https://docs.docker.com/storage/volumes/
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecs.html
- https://docs.docker.com/compose/networking/
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
- https://www.sean-lan.com/2016/09/15/django-uwsgi-nginx/
- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/java-se-nginx.html
- https://console.aws.amazon.com/vpc/home?region=us-east-1
