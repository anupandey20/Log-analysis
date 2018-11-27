# Udacity-FSND-Log-analysis

# Project Description
This project helps build an internal reporting tool that will use information from the database of a newspaper site to display reports. This reporting tool uses psycopg2 module for Python to connect to the database. It answers below questions:
1. What are the most popular three articles of all time?
2. What are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Dependencies/ Pre-requisites
1. [Python3](https://www.python.org/downloads/)
2. [Vagrant](https://www.vagrantup.com/downloads.html)
3. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
4. [Git](https://git-scm.com/downloads)

# Set up/Installation
1. Install latest Python version, VirtualBox and Vagrant.
2. Download or clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository.
3. Download the newsdata zip file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
4. Copy the content of this current repository by downloading or cloning it.

# Launching the Virtual Machine
1. Launch Vagrant VM inside Vagrant sub-directory in the downloaded repository using command:
  $ vagrant up
2. Then log into this using command:
  $ vagrant ssh
3. Change directory to /vagrant and check the files using ls.

# Setting up database
1. Load data in local database using command:
  psql -d news -f newsdata.sql
2. After loading data into database, connect to your database using:
  psql -d news
 The database includes three tables: 
- The authors table includes information about the authors of articles
- The articles table includes the articles themselves
- The log table includes one entry for each time a user has accessed the site

# Running the queries
1. To run the queries, inside the vagrant directory in VM:
  $ python3 LogAnalysisProject.py


