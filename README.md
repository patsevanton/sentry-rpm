Подготовка
```
sudo setenforce 0
sudo yum install -y epel-release rpmdevtools mc git
sudo yum install -y python-devel gcc gcc-c++ zlib-devel libjpeg-devel 
sudo yum install -y python34 python3-pip 
curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
sudo yum install -y nodejs
curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
sudo yum install -y yarn
pip3 install --user pyp2rpm
```

############ Install sentry by pip on Centos 7. неактуально
```
#pip install --upgrade pip
#pip install requests==2.20.1 -U --ignore-installed
#pip install PyYAML==3.11 -U --ignore-installed
#pip install sentry==9.1.2
```
######### 

pyp2rpm sentry -t epel7 -b2 -p2 -v 9.1.2 > sentry-9.1.2.spec
Удаляем из sentry-9.1.2.spec
```
< BuildConflicts: python2-configparser = 3.5.2
< BuildConflicts: python2-configparser = 3.5.3
< BuildConflicts: python2-configparser = 3.7.0
< BuildRequires:  python2-Babel
< BuildRequires:  python2-autopep8 < 1.4.0
< BuildRequires:  python2-autopep8 >= 1.3.5
< BuildRequires:  python2-docker < 3.8.0
< BuildRequires:  python2-docker >= 3.7.0
< BuildRequires:  python2-flake8 < 3.6.0
< BuildRequires:  python2-flake8 >= 3.5.0
< BuildRequires:  python2-isort < 4.4.0
< BuildRequires:  python2-isort >= 4.3.4
< BuildRequires:  python2-pycodestyle < 2.4.0
< BuildRequires:  python2-pycodestyle >= 2.3.1
< BuildRequires:  python2-sentry-flake8 >= 0.0.1
< BuildRequires:  python2-setuptools
```

Оставляем только 1 BuildRequires
```
BuildRequires:  python2-devel
BuildRequires:  nodejs
BuildRequires:  yarn
```

sudo yum-builddep -y sentry-9.1.2.spec


```
git clone https://github.com/getsentry/sentry.git
cd sentry
git checkout releases/9.1.x
./build.sh
```

На целевой машине пытаемся установить python2-sentry-9.1.2-1.el7.noarch.rpm

Пакуем зависимости в rpm
```
sudo yum install -y epel-release rpmdevtools mc
sudo yum install -y python-devel gcc gcc-c++ zlib-devel libjpeg-devel 
sudo yum install -y python34 python3-pip 
pip3 install --user pyp2rpm
```

msgpack
```
pyp2rpm msgpack -t epel7 -b2 -p2 -v 0.6.2 > msgpack-0.6.2.spec
sudo yum-builddep -y msgpack-0.6.2.spec 
rpmbuild -bb msgpack-0.6.2.spec 
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-msgpack-0.6.2-1.el7.x86_64.rpm
```

utils
```
pyp2rpm python-utils -t epel7 -b2 -p2 -v 2.3.0 > python-utils-2.3.0.spec
sudo yum-builddep -y python-utils-2.3.0.spec 
rpmbuild -bb python-utils-2.3.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-utils-2.3.0-1.el7.noarch.rpm 
```

progressbar2
```
pyp2rpm progressbar2 -t epel7 -b2 -p2 -v 3.10.1 > progressbar2-3.10.1.spec
sudo yum-builddep -y progressbar2-3.10.1.spec 
rpmbuild -bb progressbar2-3.10.1.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-progressbar2-3.10.1-1.el7.noarch.rpm
```

petname
```
pyp2rpm petname -t epel7 -b2 -p2 -v 2.0 > petname-2.0.spec
sudo yum-builddep -y petname-2.0.spec 
rpmbuild -bb petname-2.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-petname-2.0-1.el7.noarch.rpm
```
