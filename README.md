Подготовка
```
sudo setenforce 0
sudo yum install -y epel-release rpmdevtools mc git
sudo yum install -y python-devel gcc gcc-c++ zlib-devel libjpeg-devel python2-sphinx_rtd_theme
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
Из полученного файла убираем опциональные зависимости, зависимости для разработки (dev) и тестирования (test). Их можно найти в файлах requirements-optional.txt, requirements-dev.txt, requirements-test.txt

Это все исправил в репозитории sentry-rpm
```
git clone https://github.com/patsevanton/sentry-rpm.git
cd sentry-rpm
./build.sh
```
На целевой машине пытаемся установить python2-sentry-9.1.2-1.el7.noarch.rpm

```
sudo yum install RPMS/noarch/python2-sentry-9.1.2-1.el7.noarch.rpm
```

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

querystring-parser
```
pyp2rpm querystring-parser -t epel7 -b2 -p2 -v 1.2.4 > querystring-parser-1.2.4.spec
sudo yum-builddep -y querystring-parser-1.2.4.spec 
rpmbuild -bb querystring-parser-1.2.4.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-querystring-parser-1.2.4-1.el7.noarch.rpm
```

pytest-html
```
pyp2rpm pytest-html -t epel7 -b2 -p2 -v 1.9.0 > pytest-html-1.9.0.spec
sudo yum-builddep -y pytest-html-1.9.0.spec 
rpmbuild -bb pytest-html-1.9.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-pytest-html-1.9.0-1.el7.noarch.rpm
```

redis-py-cluster
```
pyp2rpm redis-py-cluster -t epel7 -b2 -p2 -v 1.3.4 > redis-py-cluster-1.3.4.spec
sudo yum-builddep -y redis-py-cluster-1.3.4.spec 
rpmbuild -bb redis-py-cluster-1.3.4.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-redis-py-cluster-1.3.4-1.el7.noarch.rpm
```

simplejson
```
pyp2rpm simplejson -t epel7 -b2 -p2 -v 3.8.2 > simplejson-3.8.2.spec
sudo yum-builddep -y simplejson-3.8.2.spec 
rpmbuild -bb simplejson-3.8.2.spec
sudo yum install -y rpmbuild/RPMS/x86_64/python2-simplejson-3.8.2-1.el7.x86_64.rpm
```

rb
```
pyp2rpm rb -t epel7 -b2 -p2 -v 1.7 > rb-1.7.spec
sudo yum-builddep -y rb-1.7.spec 
rpmbuild -bb rb-1.7.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-rb-1.7-1.el7.noarch.rpm
```

ua-parser
```
pyp2rpm ua-parser -t epel7 -b2 -p2 -v 0.7.3 > ua-parser-0.7.3.spec
sudo yum-builddep -y ua-parser-0.7.3.spec 
rpmbuild -bb ua-parser-0.7.3.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-ua-parser-0.7.3-1.el7.noarch.rpm
```

django-picklefield
```
pyp2rpm django-picklefield -t epel7 -b2 -p2 -v 0.3.2 > django-picklefield-0.3.2.spec
sudo yum-builddep -y django-picklefield-0.3.2.spec 
rpmbuild -bb django-picklefield-0.3.2.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-django-picklefield-0.3.2-1.el7.noarch.rpm
```

statsd
```
pyp2rpm statsd -t epel7 -b2 -p2 -v 3.1 > statsd-3.1.spec
sudo yum-builddep -y statsd-3.1.spec 
rpmbuild -bb statsd-3.1.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-statsd-3.1-1.el7.noarch.rpm 
```

pluggy
```
pyp2rpm pluggy -t epel7 -b2 -p2 -v 0.6.0 > pluggy-0.6.0.spec
sudo yum-builddep -y pluggy-0.6.0.spec 
rpmbuild -bb pluggy-0.6.0.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-pluggy-0.6.0-1.el7.noarch.rpm
```

colorama
```
pyp2rpm colorama -t epel7 -b2 -p2 -v 0.4.3 > colorama-0.4.3.spec
sudo yum-builddep -y colorama-0.4.3.spec 
rpmbuild -bb colorama-0.4.3.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-colorama-0.4.3-1.el7.noarch.rpm
```

more-itertools
```
pyp2rpm more-itertools -t epel7 -b2 -p2 -v 5.0.0 > more-itertools-5.0.0.spec
sudo yum-builddep -y more-itertools-5.0.0.spec 
rpmbuild -bb more-itertools-5.0.0.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-more-itertools-5.0.0-1.el7.noarch.rpm
```

certifi
```
pyp2rpm certifi -t epel7 -b2 -p2 -v 2016.9.26 > certifi-2016.9.26.spec
sudo yum-builddep -y certifi-2016.9.26.spec 
Change string "%{python2_sitelib}/%{pypi_name}-2016.09.26-py%{python2_version}.egg-info"
rpmbuild -bb certifi-2016.9.26.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-certifi-2016.9.26-1.el7.noarch.rpm
```

strict-rfc3339
```
pyp2rpm strict-rfc3339 -t epel7 -b2 -p2 -v 0.7 > strict-rfc3339-0.7.spec
sudo yum-builddep -y strict-rfc3339-0.7.spec 
Commented #%{python2_sitelib}/%{pypi_name}
rpmbuild -bb strict-rfc3339-0.7.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-strict-rfc3339-0.7-1.el7.noarch.rpm
```

setproctitle
```
pyp2rpm setproctitle -t epel7 -b2 -p2 -v 1.1.10 > setproctitle-1.1.10.spec
sudo yum-builddep -y setproctitle-1.1.10.spec 
Change string to "%{python2_sitearch}/%{pypi_name}.so"
rpmbuild -bb setproctitle-1.1.10.spec 
sudo yum install -y rpmbuild/RPMS/x86_64/python2-setproctitle-1.1.10-1.el7.x86_64.rpm
```

BeautifulSoup
```
pyp2rpm BeautifulSoup -t epel7 -b2 -p2 -v 3.2.2 > BeautifulSoup-3.2.2.spec
sudo yum-builddep -y BeautifulSoup-3.2.2.spec 
Commented "%{python2_sitelib}/%{pypi_name}"
rpmbuild -bb BeautifulSoup-3.2.2.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-BeautifulSoup-3.2.2-1.el7.noarch.rpm
```

Conflict:

pycparser
```
pyp2rpm pycparser -t epel7 -b2 -p2 -v 2.19 > pycparser-2.19.spec
sudo yum-builddep -y pycparser-2.19.spec 
Add %global python2_sitearch /usr/lib/python2.7/site-packages
rpmbuild -bb pycparser-2.19.spec 
sudo yum install -y rpmbuild/RPMS/x86_64/python2-pycparser-2.19-1.el7.x86_64.rpm
Conflict python-pycparser-2.14-1.el7.noarch
```

Pillow
```
pyp2rpm Pillow -t epel7 -b2 -p2 -v 4.2.1 > Pillow-4.2.1.spec
sudo yum-builddep -y Pillow-4.2.1.spec 
rpmbuild -bb Pillow-4.2.1.spec 
Conflict python-pillow-2.0.0-19.gitd1c6db8.el7.x86_64
```

chardet
```
pyp2rpm chardet -t epel7 -b2 -p2 -v 3.0.4 > chardet-3.0.4.spec
sudo yum-builddep -y chardet-3.0.4.spec 
rpmbuild -bb chardet-3.0.4.spec 
Conflict python-chardet-2.2.1-3.el7.noarch
```



Need requirements:

milksnake
```
pyp2rpm milksnake -t epel7 -b2 -p2 -v 0.1.5 > milksnake-0.1.5.spec
sudo yum-builddep -y milksnake-0.1.5.spec 
rpmbuild -bb milksnake-0.1.5.spec 
Ошибка: Пакет: python2-milksnake-0.1.5-1.el7.noarch (/python2-milksnake-0.1.5-1.el7.noarch)
            Необходимо: python2-cffi >= 1.6.0
```

setuptools
```
pyp2rpm setuptools -t epel7 -b2 -p2 -v 30.1.0 > setuptools-30.1.0.spec
sudo yum-builddep -y setuptools-30.1.0.spec 
rpmbuild -bb setuptools-30.1.0.spec 
Error: Пакет python2-certifi = 2016.9.26 не найден
Error: Пакет python2-wincertstore = 0.2 не найден
```

setuptools-scm
```
pyp2rpm setuptools-scm -t epel7 -b2 -p2 -v 3.5.0 > setuptools-scm-3.5.0.spec
sudo yum-builddep -y setuptools-scm-3.5.0.spec 
rpmbuild -bb setuptools-scm-3.5.0.spec
setuptools_scm.version.SetuptoolsOutdatedWarning: your setuptools is too old (<12)
```

py
```
pyp2rpm py -t epel7 -b2 -p2 -v 1.8.1 > py-1.8.1.spec
sudo yum-builddep -y py-1.8.1.spec 
rpmbuild -bb py-1.8.1.spec 
Error: Пакет python2-setuptools-scm не найден
```


pytest
```
pyp2rpm pytest -t epel7 -b2 -p2 -v 3.5.1 > pytest-3.5.1.spec
sudo yum-builddep -y pytest-3.5.1.spec 
rpmbuild -bb pytest-3.5.1.spec 
Error: Пакет python2-colorama не найден
Error: Пакет python2-more-itertools >= 4.0.0 не найден
Error: Пакет python2-pluggy < 0.7 не найден
Error: Пакет python2-pluggy >= 0.5 не найден
Error: Пакет python2-py >= 1.5.0 не найден
Error: Пакет python2-setuptools-scm не найден
Error: Пакет python2-six >= 1.10.0 не найден
```

semaphore
```
pyp2rpm semaphore -t epel7 -b2 -p2 -v 0.4.65 > semaphore-0.4.65.spec
sudo yum-builddep -y semaphore-0.4.65.spec 
rpmbuild -bb semaphore-0.4.65.spec 
Error: Пакет python2-milksnake >= 0.1.2 не найден
```

python-dateutil
```
pyp2rpm python-dateutil -t epel7 -b2 -p2 -v 2.8.1 > python-dateutil-2.8.1.spec
sudo yum-builddep -y python-dateutil-2.8.1.spec 
rpmbuild -bb python-dateutil-2.8.1.spec 
Error: Пакет python2-setuptools-scm не найден
```

percy
```
pyp2rpm percy -t epel7 -b2 -p2 -v 2.0.2 > percy-2.0.2.spec
sudo yum-builddep -y percy-2.0.2.spec 
rpmbuild -bb percy-2.0.2.spec 
Error: Пакет python2-requests >= 2.14.0 не найден
```

celery
```
pyp2rpm celery -t epel7 -b2 -p2 -v 3.1.18 > celery-3.1.18.spec
sudo yum-builddep -y celery-3.1.18.spec 
rpmbuild -bb celery-3.1.18.spec 
Error: Пакет python2-PyYAML >= 3.10 не найден
Error: Пакет python2-beanstalkc не найден
Error: Пакет python2-billiard < 3.4 не найден
Error: Пакет python2-couchbase не найден
Error: Пакет python2-couchdb не найден
Error: Пакет python2-gevent не найден
Error: Пакет python2-kazoo >= 1.3.1 не найден
Error: Пакет python2-kombu < 3.1 не найден
Error: Пакет python2-librabbitmq >= 1.6.1 не найден
Error: Пакет python2-pyOpenSSL не найден
Error: Пакет python2-pycassa не найден
Error: Пакет python2-pylibmc не найден
Error: Пакет python2-pymongo >= 2.6.2 не найден
Error: Пакет python2-pyro4 не найден
Error: Пакет python2-pyzmq >= 13.1.0 не найден
Error: Пакет python2-softlayer-messaging >= 1.0.3 не найден
Error: Пакет python2-sqlalchemy не найден
Error: Пакет python2-threadpool не найден
Error: Пакет python2-unittest2 >= 0.5.1 не найден

```

structlog
```
pyp2rpm structlog -t epel7 -b2 -p2 -v 16.1.0 > structlog-16.1.0.spec
sudo yum-builddep -y structlog-16.1.0.spec 
rpmbuild -bb structlog-16.1.0.spec 
Error: Пакет python2-colorama не найден
```

symbolic
```
pyp2rpm symbolic -t epel7 -b2 -p2 -v 6.1.4 > symbolic-6.1.4.spec
sudo yum-builddep -y symbolic-6.1.4.spec 
rpmbuild -bb symbolic-6.1.4.spec 
Error: Пакет python2-milksnake >= 0.1.2 не найден
```

urllib3
```
pyp2rpm urllib3 -t epel7 -b2 -p2 -v 1.24.2 > urllib3-1.24.2.spec
sudo yum-builddep -y urllib3-1.24.2.spec 
rpmbuild -bb urllib3-1.24.2.spec 
Error: Пакет python2-PySocks < 2.0 не найден
Error: Пакет python2-PySocks >= 1.5.6 не найден
Error: Пакет python2-ipaddress не найден
Error: Пакет python2-pyOpenSSL >= 0.14 не найден
```

cffi
```
pyp2rpm cffi -t epel7 -b2 -p2 -v 1.14.0 > cffi-1.14.0.spec
sudo yum-builddep -y cffi-1.14.0.spec 
rpmbuild -bb cffi-1.14.0.spec 
ошибка: Неудовлетворенные зависимости сборки:
	python2-pycparser нужен для python-cffi-1.14.0-1.el7.x86_64
```

django-crispy-forms
```
pyp2rpm django-crispy-forms -t epel7 -b2 -p2 -v 1.4.0 > django-crispy-forms-1.4.0.spec
sudo yum-builddep -y django-crispy-forms-1.4.0.spec 
rpmbuild -bb django-crispy-forms-1.4.0.spec 
Error: Пакет python2-Django < 1.6 не найден
Error: Пакет python2-Django >= 1.3 не найден
```

requests
```
pyp2rpm requests -t epel7 -b2 -p2 -v 2.20.1 > requests-2.20.1.spec
sudo yum-builddep -y requests-2.20.1.spec 
rpmbuild -bb requests-2.20.1.spec 
Error: Пакет python2-PySocks >= 1.5.6 не найден
Error: Пакет python2-chardet < 3.1.0 не найден
Error: Пакет python2-chardet >= 3.0.2 не найден
Error: Пакет python2-idna >= 2.5 не найден
Error: Пакет python2-pyOpenSSL >= 0.14 не найден
Error: Пакет python2-pytest >= 2.8.0 не найден
Error: Пакет python2-pytest-httpbin = 0.0.7 не найден
Error: Пакет python2-pytest-mock не найден
Error: Пакет python2-urllib3 >= 1.21.1 не найден
Error: Пакет python2-win-inet-pton не найден
```

oauth2
```
pyp2rpm oauth2 -t epel7 -b2 -p2 -v 1.9.0.post1 > oauth2-1.9.0.post1.spec
sudo yum-builddep -y oauth2-1.9.0.post1.spec 
rpmbuild -bb oauth2-1.9.0.post1.spec 
ошибка: Неудовлетворенные зависимости сборки:
	python2-coverage нужен для python-oauth2-1.9.0.post1-1.el7.noarch
	python2-httplib2 нужен для python-oauth2-1.9.0.post1-1.el7.noarch
```

kombu
```
pyp2rpm kombu -t epel7 -b2 -p2 -v 3.0.35 > kombu-3.0.35.spec
sudo yum-builddep -y kombu-3.0.35.spec 
rpmbuild -bb kombu-3.0.35.spec 
Error: Пакет python2-PyYAML >= 3.10 не найден
Error: Пакет python2-amqp < 2.0 не найден
Error: Пакет python2-anyjson >= 0.3.3 не найден
Error: Пакет python2-beanstalkc не найден
Error: Пакет python2-couchdb не найден
Error: Пакет python2-importlib не найден
Error: Пакет python2-kazoo >= 1.3.1 не найден
Error: Пакет python2-librabbitmq >= 1.6.1 не найден
Error: Пакет python2-ordereddict не найден
Error: Пакет python2-pymongo >= 2.6.2 не найден
Error: Пакет python2-pyro4 не найден
Error: Пакет python2-pyzmq >= 13.1.0 не найден
Error: Пакет python2-qpid-tools >= 0.26 не найден
Error: Пакет python2-softlayer-messaging >= 1.0.3 не найден
Error: Пакет python2-sqlalchemy не найден
Error: Пакет python2-unittest2 >= 0.5.0 не найден
```

PyJWT
```
pyp2rpm PyJWT -t epel7 -b2 -p2 -v 1.5.3 > PyJWT-1.5.3.spec
sudo yum-builddep -y PyJWT-1.5.3.spec 
rpmbuild -bb PyJWT-1.5.3.spec 
Error: Пакет python2-flake8 не найден
Error: Пакет python2-flake8-import-order не найден
Error: Пакет python2-pep8-naming не найден
Error: Пакет python2-pytest > 3 не найден
```

python-u2flib-server
```
pyp2rpm python-u2flib-server -t epel7 -b2 -p2 -v 4.0.1 > python-u2flib-server-4.0.1.spec
sudo yum-builddep -y python-u2flib-server-4.0.1.spec 
rpmbuild -bb python-u2flib-server-4.0.1.spec 
Error: Пакет python2-WebOb не найден
Error: Пакет python2-argparse не найден
Error: Пакет python2-yubiauth не найден
```

django-jsonfield
```
pyp2rpm django-jsonfield -t epel7 -b2 -p2 -v 0.9.13 > django-jsonfield-0.9.13.spec
sudo yum-builddep -y django-jsonfield-0.9.13.spec 
rpmbuild -bb django-jsonfield-0.9.13.spec 
ImportError: No module named django
```

loremipsum
```
pyp2rpm loremipsum -t epel7 -b2 -p2 -v 1.0.5 > loremipsum-1.0.5.spec
sudo yum-builddep -y loremipsum-1.0.5.spec 
rpmbuild -bb loremipsum-1.0.5.spec 
ImportError: No module named tests
```

mock
```
pyp2rpm mock -t epel7 -b2 -p2 -v 2.0.0 > mock-2.0.0.spec
sudo yum-builddep -y mock-2.0.0.spec 
rpmbuild -bb mock-2.0.0.spec 
	python2-pbr >= 1.3 нужен для python-mock-2.0.0-1.el7.noarch
	python2-setuptools >= 17.1 нужен для python-mock-2.0.0-1.el7.noarch
```


lxml
```
pyp2rpm lxml -t epel7 -b2 -p2 -v 4.5.0 > lxml-4.5.0.spec
sudo yum-builddep -y lxml-4.5.0.spec 
rpmbuild -bb lxml-4.5.0.spec 
Error: Пакет python2-BeautifulSoup4 не найден
Error: Пакет python2-Cython >= 0.29.7 не найден
Error: Пакет python2-cssselect >= 0.7 не найден
Error: Пакет python2-html5lib не найден
```

flake8
```
pyp2rpm flake8 -t epel7 -b2 -p2 -v 3.5.0 > flake8-3.5.0.spec
sudo yum-builddep flake8-3.5.0.spec
rpmbuild -bb flake8-3.5.0.spec
Error: Пакет python2-mock >= 2.0.0 не найден
Error: Пакет python2-pycodestyle < 2.4.0 не найден
Error: Пакет python2-setuptools >= 30 не найден
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

Failed RPM build errors:


cssutils
```
pyp2rpm cssutils -t epel7 -b2 -p2 -v 0.9.10 > cssutils-0.9.10.spec
sudo yum-builddep -y cssutils-0.9.10.spec 
rpmbuild -bb cssutils-0.9.10.spec 
FAILED (failures=3)
ошибка: Неверный код возврата из /var/tmp/rpm-tmp.wDbJ8G (%check)
```


uWSGI
```
pyp2rpm uWSGI -t epel7 -b2 -p2 -v 2.0.18 > uWSGI-2.0.18.spec
sudo yum-builddep -y uWSGI-2.0.18.spec 
rpmbuild -bb uWSGI-2.0.18.spec 
ERROR   0001: file '/usr/bin/uwsgi' contains a standard rpath '/usr/lib64' in [/usr/lib64]
```

qrcode
```
pyp2rpm qrcode -t epel7 -b2 -p2 -v 5.3 > qrcode-5.3.spec
sudo yum-builddep -y qrcode-5.3.spec 
rpmbuild -bb qrcode-5.3.spec 
error: Installed (but unpackaged) file(s) found:
   /usr/share/man/man1/qr.1.gz
```



psycopg2-binary
```
pyp2rpm psycopg2-binary -t epel7 -b2 -p2 -v 2.7.7 > psycopg2-binary-2.7.7.spec
sudo yum-builddep -y psycopg2-binary-2.7.7.spec 
rpmbuild -bb psycopg2-binary-2.7.7.spec 
Error: pg_config executable not found.
```

email-reply-parser
```
pyp2rpm email-reply-parser -t epel7 -b2 -p2 -v 0.2.0 > email-reply-parser-0.2.0.spec
sudo yum-builddep -y email-reply-parser-0.2.0.spec 
rpmbuild -bb email-reply-parser-0.2.0.spec 
AttributeError: 'module' object has no attribute 'test_support'
```

redis
```
pyp2rpm redis -t epel7 -b2 -p2 -v 2.10.5 > redis-2.10.5.spec
sudo yum-builddep -y redis-2.10.5.spec 
rpmbuild -bb redis-2.10.5.spec 
>           raise ConnectionError(self._error_message(e))
E           ConnectionError: Error 111 connecting to 127.0.0.1:6379. Connection refused.
```

sentry-sdk
```
pyp2rpm sentry-sdk -t epel7 -b2 -p2 -v 0.14.1 > sentry-sdk-0.14.1.spec
sudo yum-builddep -y sentry-sdk-0.14.1.spec 
rpmbuild -bb sentry-sdk-0.14.1.spec 
Compiling /home/centos/rpmbuild/BUILDROOT/python-sentry-sdk-0.14.1-1.el7.x86_64/usr/lib/python2.7/site-packages/sentry_sdk/integrations/aiohttp.py ...
  File "/usr/lib/python2.7/site-packages/sentry_sdk/integrations/aiohttp.py", line 58
    async def sentry_app_handle(self, request, *args, **kwargs):
            ^
SyntaxError: invalid syntax
```

Django
```
pyp2rpm Django -t epel7 -b2 -p2 -v 1.6.11 > Django-1.6.11.spec
sudo yum-builddep -y Django-1.6.11.spec 
rpmbuild -bb Django-1.6.11.spec 
error: invalid command 'test'
```

django-sudo
```
pyp2rpm django-sudo -t epel7 -b2 -p2 -v 2.1.0 > django-sudo-2.1.0.spec
sudo yum-builddep -y django-sudo-2.1.0.spec 
rpmbuild -bb django-sudo-2.1.0.spec 
Error: Пакет python2-flake8 не найден
```

python-openid
```
pyp2rpm python-openid -t epel7 -b2 -p2 -v 2.2.5 > python-openid-2.2.5.spec
sudo yum-builddep -y python-openid-2.2.5.spec 
rpmbuild -bb python-openid-2.2.5.spec 
error: invalid command 'test'
```

functools32
```
pyp2rpm functools32 -t epel7 -b2 -p2 -v 3.2.3-2 > functools32-3.2.3-2.spec
sudo yum-builddep -y functools32-3.2.3-2.spec 
rpmbuild -bb functools32-3.2.3-2.spec 
ошибка: line 5: Illegal char '-' in: Version:        3.2.3-2
Bad spec: functools32-3.2.3-2.spec
```

selenium
```
pyp2rpm selenium -t epel7 -b2 -p2 -v 3.141.0 > selenium-3.141.0.spec
sudo yum-builddep -y selenium-3.141.0.spec 
rpmbuild -bb selenium-3.141.0.spec 
RPM build errors:
    Arch dependent binaries in noarch package
```

requests-oauthlib
```
pyp2rpm requests-oauthlib -t epel7 -b2 -p2 -v 0.3.3 > requests-oauthlib-0.3.3.spec
sudo yum-builddep -y requests-oauthlib-0.3.3.spec 
rpmbuild -bb requests-oauthlib-0.3.3.spec 
ImportError: No module named tests
```

Error File not found:



wincertstore
```
pyp2rpm wincertstore -t epel7 -b2 -p2 -v 0.2 > wincertstore-0.2.spec
sudo yum-builddep -y wincertstore-0.2.spec 
rpmbuild -bb wincertstore-0.2.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-wincertstore-0.2-1.el7.x86_64/usr/lib/python2.7/site-packages/wincertstore
```

ipaddress
```
pyp2rpm ipaddress -t epel7 -b2 -p2 -v 1.0.16 > ipaddress-1.0.16.spec
sudo yum-builddep -y ipaddress-1.0.16.spec 
rpmbuild -bb ipaddress-1.0.16.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-ipaddress-1.0.16-1.el7.x86_64/usr/lib/python2.7/site-packages/ipaddress
```

six
```
pyp2rpm six -t epel7 -b2 -p2 -v 1.10.0 > six-1.10.0.spec
sudo yum-builddep -y six-1.10.0.spec 
rpmbuild -bb six-1.10.0.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-six-1.10.0-1.el7.x86_64/usr/lib/python2.7/site-packages/six
```

croniter
```
pyp2rpm croniter -t epel7 -b2 -p2 -v 0.3.31 > croniter-0.3.31.spec
sudo yum-builddep -y croniter-0.3.31.spec 
rpmbuild -bb croniter-0.3.31.spec 
RPM build errors:
    File not found by glob: /home/centos/rpmbuild/BUILDROOT/python-croniter-0.3.31-1.el7.x86_64/usr/lib/python2.7/site-packages/croniter.py*
```

ordereddict
```
pyp2rpm ordereddict -t epel7 -b2 -p2 -v 1.1 > ordereddict-1.1.spec
sudo yum-builddep -y ordereddict-1.1.spec 
rpmbuild -bb ordereddict-1.1.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-ordereddict-1.1-1.el7.x86_64/usr/lib/python2.7/site-packages/ordereddict
```

memcached
```
pyp2rpm python-memcached -t epel7 -b2 -p2 -v 1.59 > python-memcached-1.59.spec
sudo yum-builddep -y python-memcached-1.59.spec 
rpmbuild -bb python-memcached-1.59.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-memcached-1.59-1.el7.x86_64/usr/lib/python2.7/site-packages/python-memcached
```

mmh3
```
pyp2rpm mmh3 -t epel7 -b2 -p2 -v 2.3.1 > mmh3-2.3.1.spec
sudo yum-builddep -y mmh3-2.3.1.spec 
rpmbuild -bb mmh3-2.3.1.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-mmh3-2.3.1-1.el7.x86_64/usr/lib64/python2.7/site-packages/mmh3
```

mistune
```
pyp2rpm mistune -t epel7 -b2 -p2 -v 0.8.4 > mistune-0.8.4.spec
sudo yum-builddep -y mistune-0.8.4.spec 
rpmbuild -bb mistune-0.8.4.spec 
RPM build errors:
    File not found: /home/centos/rpmbuild/BUILDROOT/python-mistune-0.8.4-1.el7.x86_64/usr/lib/python2.7/site-packages/mistune
```


