#!/bin/bash

echo "Install epel-release"
sudo yum install -y epel-release git

echo "Install dependencies"
sudo yum install -y cargo gcc gcc-c++ libffi-devel libjpeg-devel libxml2-devel \
libxslt libxslt-devel make mc openssl-devel python-devel memcached \
python-lxml python-nose python2-pip python34 rpm-build rpmdevtools \
ruby-devel rubygems zlib-devel redis xmlsec1-openssl xmlsec1 \
libtool-ltdl-devel xmlsec1-devel xmlsec1-openssl-devel openldap-devel yum-utils

echo "Install fpm"
gem install --no-document fpm
echo "For chardet==3.0.2 need setuptools>=12"
echo "For cryptography==2.8 need setuptools>=18.5"
fpm -s python -t rpm setuptools==18.5
sudo yum install -y python-setuptools-18.5-1.noarch.rpm
fpm -s python -t rpm --name python2-pip pip==20.0.2
sudo yum install -y python2-pip-20.0.2-1.noarch.rpm
