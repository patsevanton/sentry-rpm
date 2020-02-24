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

############ Install sentry by pip on Centos 7. Неактуально
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

Итоговый BuildRequires
```
BuildRequires:  python2-devel
BuildRequires:  nodejs
BuildRequires:  yarn
```

sudo yum-builddep -y sentry-9.1.2.spec

Секция %prep %build %install
```
%prep
git clone https://github.com/getsentry/sentry.git
cd sentry
git checkout releases/9.1.x
# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
cd sentry
%{__python2} setup.py build

%install
cd sentry
%{__python2} setup.py install --skip-build --root %{buildroot}
```

Или просто скачиваем репозиторий

git clone https://github.com/patsevanton/sentry-rpm.git

cd sentry-rpm

Запускаем ./build.sh

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

PyYAML
```
pyp2rpm PyYAML -t epel7 -b2 -p2 -v 3.11 > PyYAML-3.11.spec
sudo yum-builddep -y PyYAML-3.11.spec 
rpmbuild -bb PyYAML-3.11.spec
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-PyYAML-3.11-1.el7.x86_64.rpm
```

django-templatetag-sugar
```
pyp2rpm django-templatetag-sugar -t epel7 -b2 -p2 -v 1.0 > django-templatetag-sugar-1.0.spec
sudo yum-builddep -y django-templatetag-sugar-1.0.spec 
rpmbuild -bb django-templatetag-sugar-1.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-django-templatetag-sugar-1.0-1.el7.noarch.rpm
```

djangorestframework
```
pyp2rpm djangorestframework -t epel7 -b2 -p2 -v 2.4.8 > djangorestframework-2.4.8.spec
sudo yum-builddep -y djangorestframework-2.4.8.spec 
rpmbuild -bb djangorestframework-2.4.8.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-djangorestframework-2.4.8-1.el7.noarch.rpm
```

enum34
```
pyp2rpm enum34 -t epel7 -b2 -p2 -v 1.1.8 > enum34-1.1.8.spec
sudo yum-builddep -y enum34-1.1.8.spec 
rpmbuild -bb enum34-1.1.8.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-enum34-1.1.8-1.el7.noarch.rpm
```

futures
```
pyp2rpm futures -t epel7 -b2 -p2 -v 3.3.0 > futures-3.3.0.spec
sudo yum-builddep -y futures-3.3.0.spec 
rpmbuild -bb futures-3.3.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-futures-3.3.0-1.el7.noarch.rpm
```

hiredis
```
pyp2rpm hiredis -t epel7 -b2 -p2 -v 0.1.6 > hiredis-0.1.6.spec
sudo yum-builddep -y hiredis-0.1.6.spec 
rpmbuild -bb hiredis-0.1.6.spec
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-hiredis-0.1.6-1.el7.x86_64.rpm
```

parsimonious
```
pyp2rpm parsimonious -t epel7 -b2 -p2 -v 0.8.0 > parsimonious-0.8.0.spec
sudo yum-builddep -y parsimonious-0.8.0.spec 
rpmbuild -bb parsimonious-0.8.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-parsimonious-0.8.0-1.el7.noarch.rpm
```

pytest-django
```
pyp2rpm pytest-django -t epel7 -b2 -p2 -v 2.9.1 > pytest-django-2.9.1.spec
sudo yum-builddep -y pytest-django-2.9.1.spec 
rpmbuild -bb pytest-django-2.9.1.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-pytest-django-2.9.1-1.el7.noarch.rpm
```

toronado
```
pyp2rpm toronado -t epel7 -b2 -p2 -v 0.0.11 > toronado-0.0.11.spec
sudo yum-builddep -y toronado-0.0.11.spec 
rpmbuild -bb toronado-0.0.11.spec 
Error: Пакет python2-cssselect не найден
Error: Пакет python2-cssutils не найден
Error: Пакет python2-exam не найден
Error: Пакет python2-flake8 не найден
Error: Пакет python2-lxml не найден
```


Need requirements:

jsonschema
```
pyp2rpm jsonschema -t epel7 -b2 -p2 -v 2.6.0 > jsonschema-2.6.0.spec
sudo yum-builddep -y jsonschema-2.6.0.spec 
rpmbuild -bb jsonschema-2.6.0.spec 
	python2-functools32 нужен для python-jsonschema-2.6.0-1.el7.noarch
	python2-rfc3987 нужен для python-jsonschema-2.6.0-1.el7.noarch
	python2-strict-rfc3339 нужен для python-jsonschema-2.6.0-1.el7.noarch
	python2-webcolors нужен для python-jsonschema-2.6.0-1.el7.noarch
```


confluent-kafka
```
pyp2rpm confluent-kafka -t epel7 -b2 -p2 -v 0.11.5 > confluent-kafka-0.11.5.spec
sudo yum-builddep -y confluent-kafka-0.11.5.spec 
rpmbuild -bb confluent-kafka-0.11.5.spec 
Error: Пакет python2-avro не найден
Error: Пакет python2-fastavro не найден
Error: Пакет python2-flake8 не найден
```

honcho
```
pyp2rpm honcho -t epel7 -b2 -p2 -v 1.0.1 > honcho-1.0.1.spec
sudo yum-builddep -y honcho-1.0.1.spec 
rpmbuild -bb honcho-1.0.1.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-honcho-1.0.1-1.el7.noarch.rpm
Ошибка: Пакет: python2-honcho-1.0.1-1.el7.noarch (/python2-honcho-1.0.1-1.el7.noarch)
            Необходимо: python2-argparse
Ошибка: Пакет: python2-honcho-1.0.1-1.el7.noarch (/python2-honcho-1.0.1-1.el7.noarch)
            Необходимо: python2-colorama
Ошибка: Пакет: python2-honcho-1.0.1-1.el7.noarch (/python2-honcho-1.0.1-1.el7.noarch)
            Необходимо: python2-ordereddict
```

botocore
```
pyp2rpm botocore -t epel7 -b2 -p2 -v 1.5.70 > botocore-1.5.70.spec
sudo yum-builddep -y botocore-1.5.70.spec 
rpmbuild -bb botocore-1.5.70.spec 
Error: Пакет python2-dateutil >= 2.1 не найден
Error: Пакет python2-ordereddict = 1.1 не найден
Error: Пакет python2-simplejson = 3.3.0 не найден
```

boto3
```
pyp2rpm boto3 -t epel7 -b2 -p2 -v 1.4.5 > boto3-1.4.5.spec
sudo yum-builddep -y boto3-1.4.5.spec 
rpmbuild -bb boto3-1.4.5.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-boto3-1.4.5-1.el7.noarch.rpm
Ошибка: Пакет: python2-boto3-1.4.5-1.el7.noarch (/python2-boto3-1.4.5-1.el7.noarch)
            Необходимо: python2-s3transfer < 0.2.0
            Доступно: python2-s3transfer-0.1.10-1.el7.noarch (epel)
                python2-s3transfer = 0.1.10-1.el7
Ошибка: Пакет: python2-boto3-1.4.5-1.el7.noarch (/python2-boto3-1.4.5-1.el7.noarch)
            Необходимо: python2-botocore < 1.6.0
            Доступно: python2-botocore-1.6.0-1.el7.noarch (epel)
                python2-botocore = 1.6.0-1.el7
Ошибка: Пакет: python2-boto3-1.4.5-1.el7.noarch (/python2-boto3-1.4.5-1.el7.noarch)
            Необходимо: python2-s3transfer >= 0.1.10
            Доступно: python2-s3transfer-0.1.10-1.el7.noarch (epel)
                python2-s3transfer = 0.1.10-1.el7
Ошибка: Пакет: python2-boto3-1.4.5-1.el7.noarch (/python2-boto3-1.4.5-1.el7.noarch)
            Необходимо: python2-botocore < 1.6.0
            Установка: python2-botocore-1.6.0-1.el7.noarch (epel)
                python2-botocore = 1.6.0-1.el7
```

Failed RPM build errors File not found:

ipaddress
```
pyp2rpm ipaddress -t epel7 -b2 -p2 -v 1.0.16 > ipaddress-1.0.16.spec
sudo yum-builddep -y ipaddress-1.0.16.spec 
rpmbuild -bb ipaddress-1.0.16.spec 
```

six
```
pyp2rpm six -t epel7 -b2 -p2 -v 1.10.0 > six-1.10.0.spec
sudo yum-builddep -y six-1.10.0.spec 
rpmbuild -bb six-1.10.0.spec 
```


croniter
```
pyp2rpm croniter -t epel7 -b2 -p2 -v 0.3.31 > croniter-0.3.31.spec
sudo yum-builddep -y croniter-0.3.31.spec 
rpmbuild -bb croniter-0.3.31.spec 
```
