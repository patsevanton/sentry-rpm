#!/bin/bash

sudo yum install -y postgresql-devel
fpm -s python -t rpm psycopg2-binary==2.7.7
sudo yum install -y python-psycopg2-binary-2.7.7-1.x86_64.rpm
yum remove -y postgresql-devel
