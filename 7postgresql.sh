#!/bin/bash

sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum install -y postgresql96 postgresql96-server postgresql96-contrib
sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb
sudo systemctl start postgresql-9.6
sudo -i -u postgres psql -c "create user sentry with password 'password';"
sudo -i -u postgres psql -c "create database sentry with owner sentry;"
sudo -i -u postgres psql -c "alter role sentry superuser;"

#sudo -i -u postgres psql -c "alter role sentry nosuperuser;"
#sudo -i -u postgres psql -c "CREATE SCHEMA main AUTHORIZATION sentry;"
