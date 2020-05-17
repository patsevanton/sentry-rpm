## Сборка sentry и его зависимостей в rpm. Установка sentry из rpm, базовая настройка.

### Описание

**Sentry** — инструмент мониторинга исключений (exception), ошибок в ваших приложениях.

**Преимущества использования Sentry:**

- не нервничать при размещении приложений на боевом сервере,
- быстро находить причины возникших проблем,
- устранять баги раньше, чем о них вам сообщат тестировщики, коллеги из саппорта, пользователи, ПМ или директор,
- выявлять незаметные остальной команде проблемы, которые портят жизнь пользователям и снижают эффективность вашего продукта,
- бесплатен,
- легко интегрируется в проект,
- ловит ошибки и в браузере пользователя, и на вашем сервере.

<cut />

**Основные возможности:**

- Список ошибок обновляется в режиме реального времени,
- Если ошибка была помечена как решенная и появилась снова, то она снова создается и учитывается в отдельном потоке,
- Ошибки группируются и отображаются в порядке частоты появления,
- Ошибки можно фильтровать по статусам, источнику логгирования, уровню логгирования, имени сервера и т.д.

Sentry поддерживает большую часть языков программирования. Подробнее [здесь](https://sentry.io/platforms/).

### Запуск Sentry с помощью docker и docker-compose

Вы можете запустить Sentry с помощью docker и docker-compose как описано здесь: https://github.com/getsentry/onpremise. Но скрипт запускает на этом же сервере в single режиме (без отказоустройчивости) дополнительные сервисы (Для версии sentry 10.0.0):

- data
- postgres
- redis
- zookeeper
- kafka
- clickhouse
- symbolicator

Если вам нужна отказоустойчивость, то вам придется либо пользоваться планым облачным продуктом, либо устанавливать Sentry без этого скрипта.

Еще один минус при запуске официального docker-compose - возможно высокая нагрузка, все сервисы запускаются на одном единственном сервере.

У вас возможно будут такие логи:

![](https://habrastorage.org/webt/e6/wp/p3/e6wpp3v64ipquyv3mqm_pzq-srk.jpeg)

![](https://habrastorage.org/webt/b1/ki/gp/b1kigpax5beos8uiyiuvqv-f65m.jpeg)

В этом посте описывается процесс сборки Sentry и его зависимостей в rpm. Если вам нужно установить Sentry там где нет интернета, то из полученных rpm можно сделать yum репозиторий.

### Важное уточение по сборке и установке пакетов

Некоторые пакеты зависят друг от друга. Поэтому процесс сборки и установки разделен на несколько этапов.

#### TODO:

В этом посте рассмотрена сборки и установка Sentry версии 9.1.2. После того как разработчики выпустят пару минорных релизов можно собирать и версию Sentry 10.X.Y. Многие последние коммиты в master - это fix (исправления).

### Требования к серверу для сборки rpm

Чем больше ЦПУ будет, тем быстрее будет происходить сборка пакетов semaphore и symbolic

### Выключаем Selinux

Сообщество будет только за, если кто-нибудь напишет политики selinux для Sentry.

```
sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
sudo reboot
```

### Подключаем репозиторий epel-release
```
sudo yum install -y epel-release git
```

### Собираем в rpm pip зависимости и устанавливаем их. Файл 1general_dependencies.sh
```
echo "Install epel-release"
sudo yum install -y epel-release

echo "Install dependencies"
sudo yum install -y cargo gcc gcc-c++ libffi-devel libjpeg-devel libxml2-devel \
libxslt libxslt-devel make mc openssl-devel python-devel memcached \
python-lxml python-nose python2-pip python34 rpm-build rpmdevtools \
ruby-devel rubygems zlib-devel redis xmlsec1-openssl xmlsec1 wget \
libtool-ltdl-devel xmlsec1-devel xmlsec1-openssl-devel openldap-devel yum-utils

echo "Install fpm"
gem install --no-document fpm
echo "For chardet==3.0.2 need setuptools>=12"
echo "For cryptography==2.8 need setuptools>=18.5"
fpm -s python -t rpm setuptools==18.5
sudo yum install -y python-setuptools-18.5-1.noarch.rpm
fpm -s python -t rpm --name python2-pip pip==20.0.2
sudo yum install -y python2-pip-20.0.2-1.noarch.rpm
```

### Устанавливаем и запускаем PostgreSQL для сборки python-psycopg2-binary. Файл 2psycopg2-binary.sh
Версию PostgreSQL вы можете поменять в скрипте.

```
sudo yum install -y postgresql-devel
fpm -s python -t rpm psycopg2-binary==2.7.7
sudo yum install -y python-psycopg2-binary-2.7.7-1.x86_64.rpm
sudo yum remove -y postgresql-devel postgresql postgresql-libs

```

### Собираем и устанавливаем python-dateutil rpm. Файл 3dateutil.sh
```
echo "Build and install python-six rpm"
fpm -s python -t rpm six==1.10.0
sudo yum install -y python-six-1.10.0-1.noarch.rpm

echo "Build and install python-dateutil rpm"
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
cp spec/python-dateutil-system-zoneinfo.patch ~/rpmbuild/SOURCES
cp spec/python-dateutil-timelex-string.patch ~/rpmbuild/SOURCES
spectool -g -R spec/python-dateutil.spec
rpmbuild -bb spec/python-dateutil.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python-dateutil-2.4.2-1.el7.noarch.rpm
```

### Собираем и устанавливаем python-urllib3 rpm. Файл 4urllib3.sh
```
echo "Install dependencies for urllib3"
fpm -s python -t rpm pycparser==2.19
sudo yum install -y python-pycparser-2.19-1.noarch.rpm
fpm -s python -t rpm cffi==1.14.0
sudo yum install -y python-cffi-1.14.0-1.x86_64.rpm
fpm -s python -t rpm cryptography==2.8
sudo yum install -y python-cryptography-2.8-1.x86_64.rpm
fpm -s python -t rpm idna==2.7
sudo yum install -y python-idna-2.7-1.noarch.rpm
sudo chmod +r /usr/lib/python2.7/site-packages/idna-2.7-py2.7.egg-info/PKG-INFO
fpm -s python -t rpm pyOpenSSL==19.1.0
sudo yum install -y python-pyopenssl-19.1.0-1.noarch.rpm
fpm -s python -t rpm pbr==5.4.4
sudo yum install -y python-pbr-5.4.4-1.noarch.rpm
fpm -s python -t rpm mock==2.0.0
sudo yum install -y python-mock-2.0.0-1.noarch.rpm
fpm -s python -t rpm py==1.8.1
sudo yum install -y python-py-1.8.1-1.noarch.rpm
fpm -s python -t rpm pluggy==0.6.0
sudo yum install -y python-pluggy-0.6.0-1.noarch.rpm
fpm -s python -t rpm attrs==19.3.0
sudo yum install -y python-attrs-19.3.0-1.noarch.rpm
fpm -s python -t rpm more-itertools==5.0.0
sudo yum install -y python-more-itertools-5.0.0-1.noarch.rpm
fpm -s python -t rpm pytest==3.5.1
sudo yum install -y python-pytest-3.5.1-1.noarch.rpm

echo "Build urllib rpm"
spectool -g -R spec/urllib3-1.24.2.spec
sudo yum-builddep -y spec/urllib3-1.24.2.spec
rpmbuild -bb spec/urllib3-1.24.2.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python-urllib3-1.24.2-1.el7.noarch.rpm
```

### Собираем в rpm остальные pip зависимости и устанавливаем их. Файл 5other_dependencies.sh
```
echo "Build rpm by fpm"
fpm -s python -t rpm jmespath==0.9.5
sudo yum install -y python-jmespath-0.9.5-1.noarch.rpm
fpm -s python -t rpm amqp==1.4.9
sudo yum install -y python-amqp-1.4.9-1.noarch.rpm
fpm -s python -t rpm anyjson==0.3.3
sudo yum install -y python-anyjson-0.3.3-1.noarch.rpm
fpm -s python -t rpm billiard==3.3.0.23
sudo yum install -y python-billiard-3.3.0.23-1.x86_64.rpm
fpm -s python -t rpm docutils==0.16
sudo yum install -y python-docutils-0.16-1.noarch.rpm
fpm -s python -t rpm Pillow==4.2.1
sudo yum install -y python-pillow-4.2.1-1.x86_64.rpm
fpm -s python -t rpm botocore==1.5.70
sudo yum install -y python-botocore-1.5.70-1.noarch.rpm
fpm -s python -t rpm boto3==1.4.5
sudo yum install -y python-boto3-1.4.5-1.noarch.rpm
fpm -s python -t rpm chardet==3.0.2
sudo yum install -y python-chardet-3.0.2-1.noarch.rpm
fpm -s python -t rpm croniter==0.3.31
sudo yum install -y python-croniter-0.3.31-1.noarch.rpm
fpm -s python -t rpm cssselect==1.1.0
sudo yum install -y python-cssselect-1.1.0-1.noarch.rpm
fpm -s python -t rpm cssutils==0.9.10
sudo yum install -y python-cssutils-0.9.10-1.noarch.rpm
fpm -s python -t rpm django-crispy-forms==1.4.0
sudo yum install -y python-django-crispy-forms-1.4.0-1.noarch.rpm
fpm -s python -t rpm django-jsonfield==0.9.13
sudo yum install -y python-django-jsonfield-0.9.13-1.noarch.rpm
fpm -s python -t rpm django-picklefield==0.3.2
sudo yum install -y python-django-picklefield-0.3.2-1.noarch.rpm
fpm -s python -t rpm django-sudo==2.1.0
sudo yum install -y python-django-sudo-2.1.0-1.noarch.rpm
fpm -s python -t rpm django-templatetag-sugar==1.0
sudo yum install -y python-django-templatetag-sugar-1.0-1.noarch.rpm
fpm -s python -t rpm djangorestframework==2.4.8
sudo yum install -y python-djangorestframework-2.4.8-1.noarch.rpm
fpm -s python -t rpm email-reply-parser==0.2.0
sudo yum install -y python-email_reply_parser-0.2.0-1.noarch.rpm
fpm -s python -t rpm enum34==1.1.9
sudo yum install -y python-enum34-1.1.9-1.noarch.rpm
fpm -s python -t rpm functools32==3.2.3.post2
sudo yum install -y python-functools32-3.2.3_2-1.noarch.rpm
fpm -s python -t rpm futures==3.3.0
sudo yum install -y python-futures-3.3.0-1.noarch.rpm
fpm -s python -t rpm hiredis==0.1.6
sudo yum install -y python-hiredis-0.1.6-1.x86_64.rpm
fpm -s python -t rpm honcho==1.0.1
sudo yum install -y python-honcho-1.0.1-1.noarch.rpm
fpm -s python -t rpm httplib2==0.17.0
sudo yum install -y python-httplib2-0.17.0-1.noarch.rpm
fpm -s python -t rpm jsonschema==2.6.0
sudo yum install -y python-jsonschema-2.6.0-1.noarch.rpm
fpm -s python -t rpm kombu==3.0.35
sudo yum install -y python-kombu-3.0.35-1.noarch.rpm
fpm -s python -t rpm celery==3.1.18
sudo yum install -y python-celery-3.1.18-1.noarch.rpm
fpm -s python -t rpm loremipsum==1.0.5
sudo yum install -y python-loremipsum-1.0.5-1.noarch.rpm
fpm -s python -t rpm lxml==4.5.0
sudo yum install -y python-lxml-4.5.0-1.x86_64.rpm
fpm -s python -t rpm milksnake==0.1.5
sudo yum install -y python-milksnake-0.1.5-1.noarch.rpm
fpm -s python -t rpm mistune==0.8.4
sudo yum install -y python-mistune-0.8.4-1.noarch.rpm
fpm -s python -t rpm mmh3==2.3.1
sudo yum install -y python-mmh3-2.3.1-1.x86_64.rpm
fpm -s python -t rpm exam==0.10.6
sudo yum install -y python-exam-0.10.6-1.noarch.rpm
fpm -s python -t rpm msgpack==0.6.2
sudo yum install -y python-msgpack-0.6.2-1.x86_64.rpm
fpm -s python -t rpm oauth2==1.9.0.post1
sudo yum install -y python-oauth2-1.9.0.post1-1.noarch.rpm
fpm -s python -t rpm oauthlib==3.1.0
sudo yum install -y python-oauthlib-3.1.0-1.noarch.rpm
fpm -s python -t rpm parsimonious==0.8.0
sudo yum install -y python-parsimonious-0.8.0-1.noarch.rpm
fpm -s python -t rpm requests==2.20.1
sudo yum install -y python-requests-2.20.1-1.noarch.rpm
fpm -s python -t rpm petname==2.0
sudo yum install -y python-petname-2.0-1.noarch.rpm
fpm -s python -t rpm python-utils==2.3.0
sudo yum install -y python-utils-2.3.0-1.noarch.rpm
fpm -s python -t rpm progressbar2==3.10.1
sudo yum install -y python-progressbar2-3.10.1-1.noarch.rpm
fpm -s python -t rpm pytest-django==2.9.1
sudo yum install -y python-pytest-django-2.9.1-1.noarch.rpm
fpm -s python -t rpm pytest-html==1.9.0
sudo yum install -y python-pytest-html-1.9.0-1.noarch.rpm
fpm -s python -t rpm python-memcached==1.59
sudo yum install -y python-memcached-1.59-1.noarch.rpm
fpm -s python -t rpm python-openid==2.2.5
sudo yum install -y python-openid-2.2.5-1.noarch.rpm
fpm -s python -t rpm python-u2flib-server==4.0.1
sudo yum install -y python-u2flib-server-4.0.1-1.noarch.rpm
fpm -s python -t rpm qrcode==5.3
sudo yum install -y python-qrcode-5.3-1.noarch.rpm
fpm -s python -t rpm querystring-parser==1.2.4
sudo yum install -y python-querystring_parser-1.2.4-1.noarch.rpm
fpm -s python -t rpm redis==2.10.5
sudo yum install -y python-redis-2.10.5-1.noarch.rpm
fpm -s python -t rpm rb==1.7
sudo yum install -y python-rb-1.7-1.noarch.rpm
fpm -s python -t rpm redis-py-cluster==1.3.4
sudo yum install -y python-redis-py-cluster-1.3.4-1.noarch.rpm
fpm -s python -t rpm requests-oauthlib==0.3.3
sudo yum install -y python-requests-oauthlib-0.3.3-1.noarch.rpm
fpm -s python -t rpm percy==2.0.2
sudo yum install -y python-percy-2.0.2-1.noarch.rpm
fpm -s python -t rpm selenium==3.141.0
sudo yum install -y python-selenium-3.141.0-1.noarch.rpm
fpm -s python -t rpm semaphore==0.4.65
sudo yum install -y python-semaphore-0.4.65-1.x86_64.rpm
fpm -s python -t rpm sentry-sdk==0.14.1
sudo yum install -y python-sentry-sdk-0.14.1-1.noarch.rpm
fpm -s python -t rpm setproctitle==1.1.10
sudo yum install -y python-setproctitle-1.1.10-1.x86_64.rpm
fpm -s python -t rpm simplejson==3.8.2
sudo yum install -y python-simplejson-3.8.2-1.x86_64.rpm
fpm -s python -t rpm sqlparse==0.1.19
sudo yum install -y python-sqlparse-0.1.19-1.noarch.rpm
fpm -s python -t rpm statsd==3.1
sudo yum install -y python-statsd-3.1-1.noarch.rpm
fpm -s python -t rpm strict-rfc3339==0.7
sudo yum install -y python-strict-rfc3339-0.7-1.noarch.rpm
fpm -s python -t rpm structlog==16.1.0
sudo yum install -y python-structlog-16.1.0-1.noarch.rpm
fpm -s python -t rpm symbolic==6.1.4
sudo yum install -y python-symbolic-6.1.4-1.x86_64.rpm
fpm -s python -t rpm toronado==0.0.11
sudo yum install -y python-toronado-0.0.11-1.noarch.rpm
fpm -s python -t rpm ua-parser==0.7.3
sudo yum install -y python-ua-parser-0.7.3-1.noarch.rpm
fpm -s python -t rpm uwsgi==2.0.18
sudo yum install -y python-uwsgi-2.0.18-1.noarch.rpm
fpm -s python -t rpm -n PyYAML pyyaml==3.11
sudo yum install -y PyYAML-3.11-1.x86_64.rpm

# for LDAP
fpm -s python -t rpm pyasn1
sudo yum install -y python-pyasn1-0.4.8-1.noarch.rpm
fpm -s python -t rpm pyasn1-modules
sudo yum install -y python-pyasn1-modules-0.2.8-1.noarch.rpm
```

### Собираем в rpm sentry и устанавливаем его. Файл 6sentry.sh
```
echo "Install nodejs and yarn"
curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
sudo yum install -y nodejs
sudo sed -e '/nodesource-source/,+6d' -i /etc/yum.repos.d/nodesource-el7.repo
curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
sudo yum install -y yarn

cp spec/config.yml spec/sentry.conf.py ~/rpmbuild/SOURCES
cp spec/sentry-cron.service spec/sentry-web.service spec/sentry-worker.service ~/rpmbuild/SOURCES
spectool -g -R spec/sentry-9.1.2.spec
sudo yum-builddep -y spec/sentry-9.1.2.spec
rpmbuild -bb spec/sentry-9.1.2.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python-sentry-9.1.2-1.el7.noarch.rpm
```

#### Собираем в rpm LDAP зависимости. Файл 7sentry-ldap-auth.sh
```
echo "Build django-auth-ldap to rpm"
spectool -g -R spec/django-auth-ldap-1.2.17.spec
sudo yum-builddep -y spec/django-auth-ldap-1.2.17.spec
rpmbuild -bb spec/django-auth-ldap-1.2.17.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-django-auth-ldap-1.2.17-1.el7.noarch.rpm

echo "Build sentry-ldap-auth to rpm"
spectool -g -R spec/sentry-ldap-auth-2.8.1.spec
sudo yum-builddep -y spec/sentry-ldap-auth-2.8.1.spec
rpmbuild -bb spec/sentry-ldap-auth-2.8.1.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-sentry-ldap-auth-2.8.1-1.el7.noarch.rpm
```

#### Устанавливаем и запускаем PostgreSQL 9.6. Файл 8postgresql.sh
```
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo yum install -y postgresql96 postgresql96-server postgresql96-contrib
sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb
sudo systemctl start postgresql-9.6
sudo -i -u postgres psql -c "create user sentry with password 'password';"
sudo -i -u postgres psql -c "create database sentry with owner sentry;"
sudo -i -u postgres psql -c "alter role sentry superuser;"

# TODO: Проверить без прав superuser для роли sentry
#sudo -i -u postgres psql -c "alter role sentry nosuperuser;"
#sudo -i -u postgres psql -c "CREATE SCHEMA main AUTHORIZATION sentry;"
```

#### Запуск тестового LDAP или подключение к рабочему LDAP (Active Directory)
Если вы хотите протестировать LDAP, то запускаем тестовый openldap в docker.
sudo docker run -p 389:389 -p 636:636 --name test-ldap --detach gitea/test-openldap
Добавляем тестовые или рабочие настройки LDAP в файл sentry.conf.py (пример ниже).

```
#############

# LDAP auth #

#############

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfUniqueNamesType

AUTH_LDAP_SERVER_URI = 'ldap://192.168.88.244:389'
#AUTH_LDAP_BIND_DN = 'admin'
#AUTH_LDAP_BIND_PASSWORD = 'GoodNewsEveryone'

AUTH_LDAP_BIND_DN = 'cn=admin,dc=planetexpress,dc=com'
AUTH_LDAP_BIND_PASSWORD = 'GoodNewsEveryone'

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'dc=planetexpress,dc=com',
    ldap.SCOPE_SUBTREE,
    '(uid=%(user)s)',
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    '',
    ldap.SCOPE_SUBTREE,
    '(objectClass=groupOfUniqueNames)'
)

AUTH_LDAP_GROUP_TYPE = GroupOfUniqueNamesType()
AUTH_LDAP_REQUIRE_GROUP = None
AUTH_LDAP_DENY_GROUP = None

AUTH_LDAP_USER_ATTR_MAP = {
    'name': 'cn',
    'email': 'mail'
}

AUTH_LDAP_FIND_GROUP_PERMS = False
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

AUTH_LDAP_DEFAULT_SENTRY_ORGANIZATION = u'Sentry'
AUTH_LDAP_SENTRY_ORGANIZATION_ROLE_TYPE = 'member'
AUTH_LDAP_SENTRY_ORGANIZATION_GLOBAL_ACCESS = True
AUTH_LDAP_SENTRY_SUBSCRIBE_BY_DEFAULT = True

SENTRY_MANAGED_USER_FIELDS = ('email', 'first_name', 'last_name', 'password', )

AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
    'sentry_ldap_auth.backend.SentryLdapBackend',
)
```

Убеждаемся в вебе под административной учётной записью по адресу, например http://ip-где-установлен-sentry:9000/manage/status/packages/, что новые пакеты с некоторыми зафиксированными версиями установлены.

Присутствует в AUTHENTICATION_BACKENDS новая запись: sentry_ldap_auth.backend.SentryLdapBackend по адресу http://ip-где-установлен-sentry:9000/manage/status/environment/

Пробуем ввести связку логин-пароль из базы LDAP, например professor professor.

Убеждаемся, что уже пользователь в организация Sentry, и соотвтетсвенно смог залогиниться.

![](https://habrastorage.org/webt/i1/jx/li/i1jxli9gj1goc6x3xql_sfxxm9c.png)

#### Запускаем миграцию (создание схемы БД) и запускаем сервисы. Файл 9start_sentry.sh
```
sudo systemctl start redis
sudo -i -u sentry /usr/bin/sentry --config /etc/sentry/ upgrade
sudo systemctl start sentry-worker
sudo systemctl start sentry-cron
sudo systemctl start sentry-web
```

#### Создаем внутреннего администратора Sentry (Если вы не создали админа при запуске 9start_sentry.sh)
https://forum.sentry.io/t/noninteractive-first-time-setup-of-user-via-upgrade/164

```
sudo -i -u sentry /usr/bin/sentry --config /etc/sentry/ createuser 
```

### Сборка sentry в rpm, установка, настройка для ленивых

#### Выключаем Selinux

```
sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
sudo reboot
```

#### Запускаем скрипты для сборки и установки sentry
```
sudo yum install -y epel-release git
git clone https://github.com/patsevanton/sentry-rpm.git
cd sentry-rpm
./1general_dependencies.sh
./2psycopg2-binary.sh
./3dateutil.sh
./4urllib3.sh
./5other_dependencies.sh
./6sentry.sh
./7sentry-ldap-auth.sh
Копируем rpm из rpmbuild/RPMS и корня sentry-rpm на целевой сервер. Создаем yum репо. Устанавливаем все собранные rpm пакеты.
./8postgresql.sh
Если вы хотите протестировать LDAP, то запускаем тестовый openldap в docker.
sudo docker run -p 389:389 -p 636:636 --name test-ldap --detach gitea/test-openldap
Добавляем тестовые или рабочие настройки LDAP в файл sentry.conf.py (пример ниже).
./9start_sentry.sh
```

#### Создаем внутреннего администратора Sentry
https://forum.sentry.io/t/noninteractive-first-time-setup-of-user-via-upgrade/164

```
sudo -i -u sentry /usr/bin/sentry --config /etc/sentry/ createuser 
```

### Тестирование отправки exception

Тестировать будем на java проекте. Скачиваем java и maven.

```
sudo yum install -y java-1.8.0-openjdk-devel git
sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
sudo yum -y install apache-maven
git clone https://github.com/getsentry/examples.git
cd examples/java/basic
mvn compile exec:java
```

Теперь нам нужно запустить java передав ему SENTRY_DSN

```
SENTRY_DSN=https://public:private@host:port/1 mvn exec:java
```

Теперь нужно найти сгенерированный по умолчанию SENTRY_DSN.

Заходим в Sentry. Идем в проект по умолчанию `internal.`

![](https://habrastorage.org/webt/ma/ky/fr/makyfr6cc2hqt6jb7vcf1hbdsly.png)

или

![](https://habrastorage.org/webt/s-/2b/lc/s-2blc7p7dnfzsi_anrohoqbc94.png)

Переходим в настройки проекта.

![](https://habrastorage.org/webt/7u/aj/vp/7uajvp33t_nq2ensgcemzbgqnta.png)

Переходим в Client Keys (DSN).

![](https://habrastorage.org/webt/el/zm/rm/elzmrmybo3fxnpilx_r5mv7r3hs.png)


Копируем DSN. Это и есть SENTRY_DSN.

![](https://habrastorage.org/webt/xl/er/d-/xlerd-ik8pi1z7by6tnzpid31fq.png)

Запускаем java с этим параметром.

```
SENTRY_DSN=http://633e7361061d4dcaaca53877c4c0e80a@172.26.9.34:9000/1 mvn exec:java
```

Видим такую картину.

![](https://habrastorage.org/webt/kh/nt/j3/khntj3xyg36qmff7mjccr8-wfs0.png)

Если перейдем в  `UnsupportedOperationException`, то увидем расширенную информацию.

![](https://habrastorage.org/webt/qx/zw/ag/qxzwagb686t-kqvdevoummsqwyc.png)

![](https://habrastorage.org/webt/vj/as/db/vjasdbflhpocxv3gsklbduwdofu.png)

#### Создал Telegram чат по Sentry

https://t.me/sentry_ru

#### В следующих сериях: 

- Протестировать sentry версию 10.0.X после того как выкатят пару минорных релизов.
