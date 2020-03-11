## Подготовка
```
sudo setenforce 0
sudo yum install -y epel-release rpmdevtools mc git 
sudo yum install -y python34 python3-pip 
curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
sudo yum install -y nodejs
curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
pip3 install --user git+https://github.com/kspby/pyp2rpm.git
```

### Формирование sentry-9.1.2.spec
```
pyp2rpm sentry -t epel7 -b2 -p2 -v 9.1.2 > sentry-9.1.2.spec
```

Удаляем из sentry-9.1.2.spec
```
sed '/python2-configparser/d' -i sentry-9.1.2.spec
sed '/python2-Babel/d' -i sentry-9.1.2.spec
sed '/python2-autopep8/d' -i sentry-9.1.2.spec
sed '/python2-docker/d' -i sentry-9.1.2.spec
sed '/python2-flake8/d' -i sentry-9.1.2.spec
sed '/python2-isort/d' -i sentry-9.1.2.spec
sed '/python2-pycodestyle/d' -i sentry-9.1.2.spec
sed '/python2-sentry-flake8/d' -i sentry-9.1.2.spec
sed '/python2-setuptools/d' -i sentry-9.1.2.spec
```

Добавляем nodejs и yarn в BuildRequires
```
sed  '/BuildRequires:  python2-devel/a BuildRequires:  nodejs >= 8' -i sentry-9.1.2.spec
sed  '/BuildRequires:  python2-devel/a BuildRequires:  yarn' -i sentry-9.1.2.spec
```

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


# remove %doc src/sentry/pipeline/README.md src/sentry/logging/README.rst src/sentry/nodestore/README.rst README.rst
```
Из полученного файла убираем опциональные зависимости, зависимости для разработки (dev) и тестирования (test). Их можно найти в файлах requirements-optional.txt, requirements-dev.txt, requirements-test.txt

### Сборка sentry-rpm без выше указанных процедур
Это все исправил в репозитории sentry-rpm
```
git clone https://github.com/patsevanton/sentry-rpm.git
cd sentry-rpm
./build.sh
```

### Установка зависимостей для сборки sentry-9.1.2.spec (то что указано в BuildRequires)
```
sudo yum-builddep -y sentry-9.1.2.spec
```

### Сборка sentry-9.1.2
```
rpmbuild -bb sentry-9.1.2.spec
```

### Попытка установки python2-sentry-9.1.2-1.el7.noarch.rpm
Нацелевой машине пытаемся установить python2-sentry-9.1.2-1.el7.noarch.rpm

```
sudo yum install rpmbuild/RPMS/noarch/python2-sentry-9.1.2-1.el7.noarch.rpm
```

## Пакуем зависимости в rpm
### Подготовка 
```
sudo yum install -y epel-release rpmdevtools mc
sudo yum install -y python-devel gcc gcc-c++ zlib-devel libjpeg-devel 
sudo yum install -y python34 python3-pip 
pip3 install --user pyp2rpm
```

### Прямые зависимости от Sentry (то что указано в https://github.com/getsentry/sentry/blob/releases/9.1.x/requirements-base.txt), которые собираются и не выдают ошибок.

msgpack
```
pyp2rpm msgpack -t epel7 -b2 -p2 -v 0.6.2 > msgpack-0.6.2.spec
rpmbuild -bb msgpack-0.6.2.spec 
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-msgpack-0.6.2-1.el7.x86_64.rpm
```

petname
```
pyp2rpm petname -t epel7 -b2 -p2 -v 2.0 > petname-2.0.spec
rpmbuild -bb petname-2.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-petname-2.0-1.el7.noarch.rpm
```

PyYAML - проверить /usr/lib64/python2.7/
```
pyp2rpm PyYAML -t epel7 -b2 -p2 -v 3.11 > PyYAML-3.11.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i PyYAML-3.11.spec
sed -e '/%description -n python2-%{pypi_name}/,+6d' -i PyYAML-3.11.spec
sed s/python2-%{pypi_name}/%{pypi_name}/g -i PyYAML-3.11.spec
sed s/python-%{pypi_name}/%{pypi_name}/g -i PyYAML-3.11.spec
sudo yum-builddep -y PyYAML-3.11.spec 
rpmbuild -bb PyYAML-3.11.spec
sudo yum install -y ~/rpmbuild/RPMS/x86_64/PyYAML-3.11-1.el7.x86_64.rpm
yum install -y https://cbs.centos.org/kojifiles/packages/PyYAML/3.11/6.el7/x86_64/PyYAML-3.11-6.el7.x86_64.rpm
```

django-templatetag-sugar
```
pyp2rpm django-templatetag-sugar -t epel7 -b2 -p2 -v 1.0 > django-templatetag-sugar-1.0.spec
rpmbuild -bb django-templatetag-sugar-1.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-django-templatetag-sugar-1.0-1.el7.noarch.rpm
```

djangorestframework
```
pyp2rpm djangorestframework -t epel7 -b2 -p2 -v 2.4.8 > djangorestframework-2.4.8.spec
rpmbuild -bb djangorestframework-2.4.8.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-djangorestframework-2.4.8-1.el7.noarch.rpm
```

enum34
```
pyp2rpm enum34 -t epel7 -b2 -p2 -v 1.1.8 > enum34-1.1.8.spec
rpmbuild -bb enum34-1.1.8.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-enum34-1.1.8-1.el7.noarch.rpm
```

futures
```
pyp2rpm futures -t epel7 -b2 -p2 -v 3.3.0 --skip-doc-build > futures-3.3.0.spec
rpmbuild -bb futures-3.3.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-futures-3.3.0-1.el7.noarch.rpm
```

hiredis
```
pyp2rpm hiredis -t epel7 -b2 -p2 -v 0.1.6 > hiredis-0.1.6.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  gcc' -i hiredis-0.1.6.spec
sudo yum-builddep -y hiredis-0.1.6.spec 
rpmbuild -bb hiredis-0.1.6.spec
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-hiredis-0.1.6-1.el7.x86_64.rpm
```

parsimonious
```
pyp2rpm parsimonious -t epel7 -b2 -p2 -v 0.8.0 > parsimonious-0.8.0.spec
rpmbuild -bb parsimonious-0.8.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-parsimonious-0.8.0-1.el7.noarch.rpm
```

pytest-django
```
pyp2rpm pytest-django -t epel7 -b2 -p2 -v 2.9.1 --skip-doc-build > pytest-django-2.9.1.spec
rpmbuild -bb pytest-django-2.9.1.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-pytest-django-2.9.1-1.el7.noarch.rpm
```

pytest-html
```
pyp2rpm pytest-html -t epel7 -b2 -p2 -v 1.9.0 > pytest-html-1.9.0.spec
rpmbuild -bb pytest-html-1.9.0.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-pytest-html-1.9.0-1.el7.noarch.rpm
```

redis-py-cluster
```
pyp2rpm redis-py-cluster -t epel7 -b2 -p2 -v 1.3.4 > redis-py-cluster-1.3.4.spec
rpmbuild -bb redis-py-cluster-1.3.4.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-redis-py-cluster-1.3.4-1.el7.noarch.rpm
```

simplejson
```
pyp2rpm simplejson -t epel7 -b2 -p2 -v 3.8.2 > simplejson-3.8.2.spec
rpmbuild -bb simplejson-3.8.2.spec
sudo yum install -y rpmbuild/RPMS/x86_64/python2-simplejson-3.8.2-1.el7.x86_64.rpm
```

rb
```
pyp2rpm rb -t epel7 -b2 -p2 -v 1.7 > rb-1.7.spec
rpmbuild -bb rb-1.7.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-rb-1.7-1.el7.noarch.rpm
```

ua-parser
```
pyp2rpm ua-parser -t epel7 -b2 -p2 -v 0.7.3 > ua-parser-0.7.3.spec
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
pyp2rpm statsd -t epel7 -b2 -p2 -v 3.1 --skip-doc-build  > statsd-3.1.spec
sed  '/BuildRequires:  python2-devel/a BuildRequires:  python2-mock' -i statsd-3.1.spec
sudo yum-builddep -y statsd-3.1.spec 
rpmbuild -bb statsd-3.1.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-statsd-3.1-1.el7.noarch.rpm 
```

strict-rfc3339
```
pyp2rpm strict-rfc3339 -t epel7 -b2 -p2 -v 0.7 > strict-rfc3339-0.7.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i strict-rfc3339-0.7.spec
rpmbuild -bb strict-rfc3339-0.7.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-strict-rfc3339-0.7-1.el7.noarch.rpm
```

setproctitle
```
pyp2rpm setproctitle -t epel7 -b2 -p2 -v 1.1.10 > setproctitle-1.1.10.spec
sed 's/%{python2_sitearch}\/%{pypi_name}$/%{python2_sitearch}\/%{pypi_name}.so/g' -i setproctitle-1.1.10.spec
rpmbuild -bb setproctitle-1.1.10.spec 
sudo yum install -y rpmbuild/RPMS/x86_64/python2-setproctitle-1.1.10-1.el7.x86_64.rpm
```

BeautifulSoup
```
pyp2rpm BeautifulSoup -t epel7 -b2 -p2 -v 3.2.2 > BeautifulSoup-3.2.2.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i BeautifulSoup-3.2.2.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i BeautifulSoup-3.2.2.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i BeautifulSoup-3.2.2.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i BeautifulSoup-3.2.2.spec
rpmbuild -bb BeautifulSoup-3.2.2.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python-BeautifulSoup-3.2.2-1.el7.noarch.rpm
```

mistune
```
pyp2rpm mistune -t epel7 -b2 -p2 -v 0.8.4 > mistune-0.8.4.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i mistune-0.8.4.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i mistune-0.8.4.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i mistune-0.8.4.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i mistune-0.8.4.spec
rpmbuild -bb mistune-0.8.4.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python-mistune-0.8.4-1.el7.noarch.rpm
```

mmh3
```
pyp2rpm mmh3 -t epel7 -b2 -p2 -v 2.3.1 > mmh3-2.3.1.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  gcc-c++' -i mmh3-2.3.1.spec
sed 's/%{python2_sitearch}\/%{pypi_name}$/%{python2_sitearch}\/%{pypi_name}.so/g' -i mmh3-2.3.1.spec
sudo yum-builddep -y mmh3-2.3.1.spec 
rpmbuild -bb mmh3-2.3.1.spec 
sudo yum install -y rpmbuild/RPMS/x86_64/python2-mmh3-2.3.1-1.el7.x86_64.rpm
```

python-memcached
```
pyp2rpm python-memcached -t epel7 -b2 -p2 -v 1.59 > python-memcached-1.59.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i python-memcached-1.59.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i python-memcached-1.59.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i python-memcached-1.59.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i python-memcached-1.59.spec
sudo yum-builddep -y python-memcached-1.59.spec 
rpmbuild -bb python-memcached-1.59.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-memcached-1.59-1.el7.noarch.rpm
sudo yum install -y https://cbs.centos.org/kojifiles/packages/python-memcached/1.58/1.el7/noarch/python-memcached-1.58-1.el7.noarch.rpm
```

croniter
```
pyp2rpm croniter -t epel7 -b2 -p2 -v 0.3.31 > croniter-0.3.31.spec
sudo yum-builddep -y croniter-0.3.31.spec 
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i croniter-0.3.31.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i croniter-0.3.31.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i croniter-0.3.31.spec
sed "/%{python2_sitelib}\/%{pypi_name}.py\*$/d" -i croniter-0.3.31.spec
rpmbuild -bb croniter-0.3.31.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python-croniter-0.3.31-1.el7.noarch.rpm
```

### Зависимости от зависимостей Sentry, которые собираются.

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
rpmbuild -bb progressbar2-3.10.1.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-progressbar2-3.10.1-1.el7.noarch.rpm
```

querystring-parser
```
pyp2rpm querystring-parser -t epel7 -b2 -p2 -v 1.2.4 > querystring-parser-1.2.4.spec
rpmbuild -bb querystring-parser-1.2.4.spec 
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-querystring-parser-1.2.4-1.el7.noarch.rpm
```

pluggy
```
pyp2rpm pluggy -t epel7 -b2 -p2 -v 0.6.0 > pluggy-0.6.0.spec
rpmbuild -bb pluggy-0.6.0.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-pluggy-0.6.0-1.el7.noarch.rpm
```

more-itertools
```
pyp2rpm more-itertools -t epel7 -b2 -p2 -v 5.0.0 --skip-doc-build > more-itertools-5.0.0.spec
rpmbuild -bb more-itertools-5.0.0.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-more-itertools-5.0.0-1.el7.noarch.rpm
```

certifi - воможно удалить 
```
pyp2rpm certifi -t epel7 -b2 -p2 -v 2016.9.26 > certifi-2016.9.26.spec
sudo yum-builddep -y certifi-2016.9.26.spec 
Change string "%{python2_sitelib}/%{pypi_name}-2016.09.26-py%{python2_version}.egg-info"
rpmbuild -bb certifi-2016.9.26.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-certifi-2016.9.26-1.el7.noarch.rpm
python2-certifi.noarch 2018.10.15-5.el7 epel
```

### Пакеты, которые конфликтуют с уже установленными пакетами


six
```
pyp2rpm six -t epel7 -b2 -p2 -v 1.10.0 --skip-doc-build > six-1.10.0.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i six-1.10.0.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i six-1.10.0.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i six-1.10.0.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i six-1.10.0.spec
rpmbuild -bb six-1.10.0.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python-six-1.10.0-1.el7.noarch.rpm
```

pycparser
```
pyp2rpm pycparser -t epel7 -b2 -p2 -v 2.19 > pycparser-2.19.spec
sed  '/%global pypi_name pycparser/a %global python2_sitearch /usr/lib/python2.7/site-packages' -i pycparser-2.19.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i pycparser-2.19.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i pycparser-2.19.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i pycparser-2.19.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i pycparser-2.19.spec
rpmbuild -bb pycparser-2.19.spec 
sudo yum install -y rpmbuild/RPMS/x86_64/python-pycparser-2.19-1.el7.x86_64.rpm
```

Pillow
```
pyp2rpm Pillow -t epel7 -b2 -p2 -v 4.2.1 > pillow-4.2.1.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  libjpeg-devel' -i pillow-4.2.1.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  zlib-devel' -i pillow-4.2.1.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  python2-sphinx_rtd_theme' -i pillow-4.2.1.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  python-nose' -i pillow-4.2.1.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i pillow-4.2.1.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i pillow-4.2.1.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i pillow-4.2.1.spec
sed "/%{python2_sitelib}\/%{pypi_name}$/d" -i pillow-4.2.1.spec
sed 's/%global pypi_name Pillow/%global pypi_name pillow/g' -i pillow-4.2.1.spec
sed 's/%{pypi_name}\/%{pypi_name}-%{version}/Pillow\/Pillow-%{version}/g' -i pillow-4.2.1.spec
sudo yum-builddep -y pillow-4.2.1.spec 
rpmbuild -bb pillow-4.2.1.spec 
ошибка: Файл /home/centos/rpmbuild/SOURCES/pillow-4.2.1.tar.gz: Нет такого файла или каталога
sudo yum install rpmbuild/RPMS/x86_64/python2-Pillow-4.2.1-1.el7.x86_64.rpm 
```

chardet - возможно удалить
```
pyp2rpm chardet -t epel7 -b2 -p2 -v 2.2.1 > chardet-2.2.1.spec
sudo yum-builddep -y chardet-2.2.1.spec 
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i chardet-2.2.1.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i chardet-2.2.1.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i chardet-2.2.1.spec
rpmbuild -bb chardet-2.2.1.spec 
??
```

### Пакеты для которых нет зависимостей в системных репозиториях


cffi
```
pyp2rpm cffi -t epel7 -b2 -p2 -v 1.14.0 --skip-doc-build  > cffi-1.14.0.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  libffi-devel' -i cffi-1.14.0.spec
sed  '/BuildRequires:  python2-setuptools/a BuildRequires:  gcc' -i cffi-1.14.0.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i cffi-1.14.0.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i cffi-1.14.0.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i cffi-1.14.0.spec
sed s/python2-pycparser/python-pycparser/g -i cffi-1.14.0.spec
sed  '/%{python2_sitearch}\/%{pypi_name}$/a %{python2_sitearch}\/_cffi_backend.so' -i cffi-1.14.0.spec
sudo yum-builddep -y cffi-1.14.0.spec 
rpmbuild -bb cffi-1.14.0.spec 
sudo yum install -y rpmbuild/RPMS/x86_64/python-cffi-1.14.0-1.el7.x86_64.rpm
```

milksnake
```
pyp2rpm milksnake -t epel7 -b2 -p2 -v 0.1.5 > milksnake-0.1.5.spec
sed s/python2-cffi/python-cffi/g -i milksnake-0.1.5.spec
rpmbuild -bb milksnake-0.1.5.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python2-milksnake-0.1.5-1.el7.noarch.rpm
```

py
```
pyp2rpm py -t epel7 -b2 -p2 -v 1.5.1 --skip-doc-build > py-1.5.1.spec
sed '/setuptools-scm/d' -i py-1.5.1.spec
sed -e '/%package -n.*python2-%{pypi_name}/,+1d' -i py-1.5.1.spec
sed -e '/%description -n python2-%{pypi_name}/,+1d' -i py-1.5.1.spec
sed s/python2-%{pypi_name}/python-%{pypi_name}/g -i py-1.5.1.spec
rpmbuild -bb py-1.5.1.spec 
sudo yum install -y rpmbuild/RPMS/noarch/python-py-1.5.1-1.el7.noarch.rpm
```

pytest
```
pyp2rpm pytest -t epel7 -b2 -p2 -v 3.5.1 --skip-doc-build > pytest-3.5.1.spec
sed '/colorama/d' -i pytest-3.5.1.spec
sed '/setuptools-scm/d' -i pytest-3.5.1.spec
sed s/python2-six/python-six/g -i pytest-3.5.1.spec
sed s/python2-py/python-py/g -i pytest-3.5.1.spec
sudo yum-builddep -y pytest-3.5.1.spec 
rpmbuild -bb pytest-3.5.1.spec 
setuptools_scm.version.SetuptoolsOutdatedWarning: your setuptools is too old (<12)
```

semaphore
```
pyp2rpm semaphore -t epel7 -b2 -p2 -v 0.4.65 > semaphore-0.4.65.spec
sudo yum-builddep -y semaphore-0.4.65.spec 
rpmbuild -bb semaphore-0.4.65.spec 
Error: Пакет python2-milksnake >= 0.1.2 не найден
```

python-dateutil - возможно удалить
```
pyp2rpm python-dateutil -t epel7 -b2 -p2 -v 2.8.1 > python-dateutil-2.8.1.spec
sed '/setuptools-scm/d' -i python-dateutil-2.8.1.spec
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
pyp2rpm celery -t epel7 -b2 -p2 -v 3.1.18 --skip-doc-build > celery-3.1.18.spec
sed '/beanstalkc/d' -i celery-3.1.18.spec
sed '/couchbase/d' -i celery-3.1.18.spec
sed '/couchdb/d' -i celery-3.1.18.spec
sed '/gevent/d' -i celery-3.1.18.spec
sed '/kazoo/d' -i celery-3.1.18.spec
sed '/librabbitmq/d' -i celery-3.1.18.spec
sed '/pycassa/d' -i celery-3.1.18.spec
sed '/pylibmc/d' -i celery-3.1.18.spec
sed '/pymongo/d' -i celery-3.1.18.spec
sed '/pyro4/d' -i celery-3.1.18.spec
sed '/pyzmq/d' -i celery-3.1.18.spec
sed '/softlayer-messaging/d' -i celery-3.1.18.spec
sed '/sqlalchemy/d' -i celery-3.1.18.spec
sed '/threadpool/d' -i celery-3.1.18.spec
sed '/unittest2/d' -i celery-3.1.18.spec
sed '/beanstalkc/d' -i celery-3.1.18.spec
sed s/python2-PyYAML/PyYAML/g -i celery-3.1.18.spec
sed s/python2-pyOpenSSL/pyOpenSSL/g -i celery-3.1.18.spec
sed s/python2-billiard/python-billiard/g -i celery-3.1.18.spec
sudo yum install -y https://repos.fedorapeople.org/pulp/pulp/stable/2.6/7Server/x86_64/python-billiard-3.3.0.17-2.el7.x86_64.rpm
sudo yum-builddep -y celery-3.1.18.spec 
rpmbuild -bb celery-3.1.18.spec 
```

structlog
```
pyp2rpm structlog -t epel7 -b2 -p2 -v 16.1.0 > structlog-16.1.0.spec
Удалить colorama из зависимостей
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
Удалить PySocks из зависимостей
sudo yum-builddep -y urllib3-1.24.2.spec 
rpmbuild -bb urllib3-1.24.2.spec 
Error: Пакет python2-PySocks < 2.0 не найден
Error: Пакет python2-PySocks >= 1.5.6 не найден
Error: Пакет python2-ipaddress не найден
Error: Пакет python2-pyOpenSSL >= 0.14 не найден
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
Удалить PySocks из зависимостей
Удалить pytest-mock из зависимостей
Удалить win-inet-pton из зависимостей
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
Удалить coverage из зависимостей
sudo yum-builddep -y oauth2-1.9.0.post1.spec 
rpmbuild -bb oauth2-1.9.0.post1.spec 
ошибка: Неудовлетворенные зависимости сборки:
	python2-coverage нужен для python-oauth2-1.9.0.post1-1.el7.noarch
	python2-httplib2 нужен для python-oauth2-1.9.0.post1-1.el7.noarch
```

kombu
```
pyp2rpm kombu -t epel7 -b2 -p2 -v 3.0.35 > kombu-3.0.35.spec
Удалить ordereddict из зависимостей
Удалить beanstalkc из зависимостей
Удалить couchdb из зависимостей
Удалить importlib из зависимостей
Удалить librabbitmq из зависимостей
Удалить pymongo из зависимостей
Удалить pyro4 из зависимостей
Удалить pyzmq из зависимостей
Удалить qpid-tools из зависимостей
Удалить softlayer-messaging из зависимостей
Удалить sqlalchemy из зависимостей
Удалить unittest2 из зависимостей
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
Удалить flake8 из зависимостей
Удалить flake8-import-order из зависимостей
Удалить pep8-naming из зависимостей
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
Удалить WebOb из зависимостей
Удалить argparse из зависимостей
Удалить yubiauth из зависимостей
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
Удалить setuptools из зависимостей
sudo yum-builddep -y mock-2.0.0.spec 
rpmbuild -bb mock-2.0.0.spec 
	python2-pbr >= 1.3 нужен для python-mock-2.0.0-1.el7.noarch
	python2-setuptools >= 17.1 нужен для python-mock-2.0.0-1.el7.noarch
```


lxml
```
pyp2rpm lxml -t epel7 -b2 -p2 -v 4.5.0 > lxml-4.5.0.spec
Удалить BeautifulSoup4 из зависимостей
Удалить Cython из зависимостей
Удалить html5lib из зависимостей
sudo yum-builddep -y lxml-4.5.0.spec 
rpmbuild -bb lxml-4.5.0.spec 
Error: Пакет python2-BeautifulSoup4 не найден
Error: Пакет python2-Cython >= 0.29.7 не найден
Error: Пакет python2-cssselect >= 0.7 не найден
Error: Пакет python2-html5lib не найден
```

toronado
```
pyp2rpm toronado -t epel7 -b2 -p2 -v 0.0.11 > toronado-0.0.11.spec
Удалить flake8 из зависимостей
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
Удалить rfc3987 из зависимостей
Удалить webcolors из зависимостей
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
Удалить argparse из зависимостей
Удалить colorama из зависимостей
Удалить ordereddict из зависимостей
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
Удалить ordereddict из зависимостей
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

### Пакеты, которые при сборке выдают ошибку


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
