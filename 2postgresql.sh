#!/bin/bash

yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum install -y postgresql96 postgresql96-server postgresql96-contrib postgresql96-devel
/usr/pgsql-9.6/bin/postgresql96-setup initdb
systemctl start postgresql-9.6
create user sentry with password 'password';
create database sentry with owner sentry;
alter role sentry superuser;


#alter role sentry nosuperuser;
#CREATE SCHEMA main AUTHORIZATION sentry;
