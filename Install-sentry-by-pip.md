# Установка sentry через pip на Centos 7 для проверки списка зависимостей в vagrant

```
sudo yum install -y epel-release mc gcc gcc-c++ python-devel
sudo yum install -y python2-pip ca-certificates
reboot
sudo pip install requests==2.20.1 -U --ignore-installed
Successfully installed certifi-2019.11.28 chardet-2.2.1 idna-2.7 requests-2.20.1 urllib3-1.24.3

sudo pip install --upgrade pip
Successfully installed pip-20.0.2

sudo pip install PyYAML==3.11 -U --ignore-installed
Successfully installed PyYAML-3.11

sudo pip install sentry==9.1.2
```
