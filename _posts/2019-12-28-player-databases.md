---
layout: post
title: Web Scraping, SQLite, and Dead NBA players (player databases)
published: false
---

Prior to attending the 2019 NBA Hack a thon in Seacaucus, which was a wonderful experience, a few NBA sent out applications for data analytics/software engineering/analytics/etc. internships. A weekend of playing around with SQLite and some web scraping has culminated into this blog post. 

<p align="center">
<img src="https://raymondhfeng.github.io/images/nba-hackathon.jpeg" align="middle" width="200">
</p>

<h3>The Architecture</h3>
Transactions database - contains each transaction, including the player involved, the teams involved.
Players database - contains main attributes for each player

<h3>Populating the database</h3>
Just used a few different jupyter instances running at once, querying the realGM API. A problem I ran into a lot was the network timing out, and in turn, all of the entries I put into the database getting rolled back. So to solve this, I had a really ghetto "checkpointing" system, which just consisted of making 
