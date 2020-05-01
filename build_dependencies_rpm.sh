#!/bin/bash

echo "Install epel-release"
sudo yum install -y epel-release git

echo "Install dependencies"
sudo yum install -y cargo gcc gcc-c++ libffi-devel libjpeg-devel libxml2-devel \
libxslt libxslt-devel make mc openssl-devel postgresql-devel python-devel \
python-lxml python-nose python3-pip python34 rpm-build rpmdevtools \
ruby-devel rubygems zlib-devel

echo "Install fpm"
gem install --no-document fpm
echo "For chardet==3.0.2 need setuptools>=12"
echo "For cryptography==2.8 need setuptools>=18.5"
fpm -s python -t rpm setuptools==18.5
sudo yum install -y python-setuptools-18.5-1.noarch.rpm

echo "Install dependencies for urllib3"
fpm -s python -t rpm cryptography==2.8
sudo yum install -y python-cryptography-2.8-1.x86_64.rpm