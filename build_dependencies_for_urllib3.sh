#!/bin/bash

echo "Install dependencies for urllib3"
fpm -s python -t rpm pycparser==2.19
sudo yum install -y python-pycparser-2.19-1.noarch.rpm
fpm -s python -t rpm cffi==1.14.0
sudo yum install -y python-cffi-1.14.0-1.x86_64.rpm
fpm -s python -t rpm cryptography==2.8
sudo yum install -y python-cryptography-2.8-1.x86_64.rpm
fpm -s python -t rpm idna==2.7
sudo yum install -y python-idna-2.7-1.noarch.rpm
fpm -s python -t rpm pyOpenSSL==19.1.0
sudo yum install -y python-pyopenssl-19.1.0-1.noarch.rpm
fpm -s python -t rpm mock==2.0.0
sudo yum install -y python-mock-2.0.0-1.noarch.rpm
fpm -s python -t rpm pytest==3.5.1
sudo yum install -y python-pytest-3.5.1-1.noarch.rpm
