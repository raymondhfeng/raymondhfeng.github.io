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
https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

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

```

# References:
I learned how to do this by combining a number of sources. 
- 