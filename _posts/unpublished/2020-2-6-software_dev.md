---
layout: post
title: Overview of Software Development
published: true
---

<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

https://technically.dev/posts/what-your-developers-are-using.html
- SWE works in cycles
- Nobody actually knows what they are doing
- Every company is different
	* Writing code: IDE, Language, Frameworks, Package Mangers, SDKs
	* Deciding on code: Version control, CI/CD
	* Deploying code: Infrastructure, Containers and orchestration
	* Monitoring tools: Log storage, APM tools. 
- Devtools go through horizontal to vertical cycles. Startups always try and conglomerate these five tasks, but then realize that it takes too long to sell. Eventually, they try and optimize one part of this cycle. 
- Scenario: web app in React, deploying on AWS infrastructure
	* Write: code in Javascript inside VSCode, using React, Yarn, and the SnapKit SDK
	* Decide: on code using using Github and CircleCI
	* Deploy: code using EC2, RDS, Docker, and Kubernetes
	* Monitor: code using Datadog and Prometheus

## 1. Writing Code

- IDEs
	* Like Google Docs, but more for building applications
	* VSCode is the most popular right now
	* Jetbrains popular
	* Sublime and Atom are not really IDEs
- Programming Language
	* Most popular is Javascript, followed by HTML/CSS (Technically doesn't count)
	* Next up: Python, Java, C++, C#, C, PHP, Ruby, and Go
- Frameworks
	* "modules, frameworks, packages, or libraries"
	* These exist across the whole developer workflow
	* useful so that you don't have to rewrite common pieces of code
	* developers use: React, Tensorflow, Pytorch, Requests (in Python)
- Package Managers
	* Managing the dependencies of frameworks can get tedious
	* NPM, Yarn, Anaconda, Virtualenv (technically doesn't count), homebrew
- SDKs
	* Collection of APIs that you use to build something useful
	* SnapKit, Google Maps SDK, Apple's ARKit. 

## 2. Deciding on Code

- Version Control
	* Allows developers to collaborate. Like a supercharged save button in Excel. 
	* Git, Github, Gitlab, Bitbucket
- Continuous integration and delivery
	* CI: "new code changes to an app are regularly built, testted, and merged to a shared repository."
	* Adds automation to the code changes you are making: run automated tests. "Are thee security vulnerabilities? Does it break anything?" and merge/deploy your changes rapidly. 
	* CircleCI, and Jenkins. Github and co. provide similar functionality. 

## 3. Deploying Code

- IaaS
	* Cloud providers. Very little abstraction, paying for compute and storage to run your application on. 
	* AWS (EC2 and EBS)
	* GCP, Microsoft Azure, Digital Ocean
- PaaS
	* Working with bare bones compute and storage is kind of annoying. PaaS is a platform that can automatically deploy code from a GitHub repo. A lot more GUI beef for doing things in console instead of in API, charges a lot more money. 
	* Heroku, first one, got acquired by Salesforce back in the day. AWS (RDS, SQS, Lambda). Smaller companies like MongoDB, Snowflake, Elastic for storage, and Confluent and Netify for compute. 
- Containers and Orchestration
	* You can't just plop code on a server by itself, you need an environment you need to run it in. Containers and orchestrators allow you to plop software into any place that you need. 
	* Docker is the dominant container, and has their own orchestrator called Swarm, but is overshadowed by the more dominany Kubernetes. 

## Monitoring Code

- Log Storage and Visualization
	* Log data is extremely difficult to parse, and so companies exist to organize them and "glean insights". 
	* Most popular log management solution is Elasticsearch, built off of Apache Lucene. Lets you store index and search your log data. Kibana is for visualization. 

- APM tools
	* Application performance management. Holistic management of your deployed applications. Mainly SaaS providers give you fine grained insight into your application's performance. 
	* New Relic and Datadog are the two most popular APM vendors. Hook these up with your cloud providers and you will get metrics, alerts, and visualizations. Prometheus and Grafana are open source solutions. 
