#!/bin/bash

echo "Build rpm by fpm"
fpm -s python -t rpm jmespath==0.9.5
sudo yum install -y python-jmespath-0.9.5-1.noarch.rpm
fpm -s python -t rpm amqp==1.4.9
sudo yum install -y python-amqp-1.4.9-1.noarch.rpm
fpm -s python -t rpm anyjson==0.3.3
sudo yum install -y python-anyjson-0.3.3-1.noarch.rpm
fpm -s python -t rpm attrs==19.3.0
sudo yum install -y python-attrs-19.3.0-1.noarch.rpm
fpm -s python -t rpm BeautifulSoup==3.2.2
sudo yum install -y python-beautifulsoup-3.2.2-1.noarch.rpm
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
fpm -s python -t rpm click==6.7
sudo yum install -y python-click-6.7-1.noarch.rpm
fpm -s python -t rpm croniter==0.3.31
sudo yum install -y python-croniter-0.3.31-1.noarch.rpm
fpm -s python -t rpm cryptography==2.8
sudo yum install -y python-cryptography-2.8-1.x86_64.rpm
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
fpm -s python -t rpm Django==1.6.11
sudo yum install -y python-django-1.6.11-1.noarch.rpm
fpm -s python -t rpm djangorestframework==2.4.8
sudo yum install -y python-djangorestframework-2.4.8-1.noarch.rpm
fpm -s python -t rpm pycparser==2.19
sudo yum install -y python-pycparser-2.19-1.noarch.rpm
fpm -s python -t rpm cffi==1.14.0
sudo yum install -y python-cffi-1.14.0-1.x86_64.rpm
fpm -s python -t rpm email-reply-parser==0.2.0
sudo yum install -y python-email_reply_parser-0.2.0-1.noarch.rpm
fpm -s python -t rpm enum34==1.1.9
sudo yum install -y python-enum34-1.1.9-1.noarch.rpm
fpm -s python -t rpm funcsigs==1.0.2
sudo yum install -y python-funcsigs-1.0.2-1.noarch.rpm
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
fpm -s python -t rpm idna==2.7
sudo yum install -y python-idna-2.7-1.noarch.rpm
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
fpm -s python -t rpm pbr==5.4.4
sudo yum install -y python-pbr-5.4.4-1.noarch.rpm
fpm -s python -t rpm mock==2.0.0
sudo yum install -y python-mock-2.0.0-1.noarch.rpm
fpm -s python -t rpm exam==0.10.6
sudo yum install -y python-exam-0.10.6-1.noarch.rpm
fpm -s python -t rpm more-itertools==5.0.0
sudo yum install -y python-more-itertools-5.0.0-1.noarch.rpm
fpm -s python -t rpm msgpack==0.6.2
sudo yum install -y python-msgpack-0.6.2-1.x86_64.rpm
fpm -s python -t rpm oauth2==1.9.0.post1
sudo yum install -y python-oauth2-1.9.0.post1-1.noarch.rpm
fpm -s python -t rpm oauthlib==3.1.0
sudo yum install -y python-oauthlib-3.1.0-1.noarch.rpm
fpm -s python -t rpm olefile==0.46
sudo yum install -y python-olefile-0.46-1.noarch.rpm
fpm -s python -t rpm parsimonious==0.8.0
sudo yum install -y python-parsimonious-0.8.0-1.noarch.rpm
fpm -s python -t rpm requests==2.20.1
sudo yum install -y python-requests-2.20.1-1.noarch.rpm
fpm -s python -t rpm petname==2.0
sudo yum install -y python-petname-2.0-1.noarch.rpm
fpm -s python -t rpm pluggy==0.6.0
sudo yum install -y python-pluggy-0.6.0-1.noarch.rpm
fpm -s python -t rpm progressbar2==3.10.1
sudo yum install -y python-progressbar2-3.10.1-1.noarch.rpm
fpm -s python -t rpm psycopg2-binary==2.7.7
sudo yum install -y python-psycopg2-binary-2.7.7-1.x86_64.rpm
fpm -s python -t rpm py==1.8.1
sudo yum install -y python-py-1.8.1-1.noarch.rpm
fpm -s python -t rpm PyJWT==1.5.3
sudo yum install -y python-pyjwt-1.5.3-1.noarch.rpm
fpm -s python -t rpm pyOpenSSL==19.1.0
sudo yum install -y python-pyopenssl-19.1.0-1.noarch.rpm
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
fpm -s python -t rpm python-utils==2.3.0
sudo yum install -y python-utils-2.3.0-1.noarch.rpm
fpm -s python -t rpm pytz==2019.3
sudo yum install -y python-pytz-2019.3-1.noarch.rpm
fpm -s python -t rpm qrcode==5.3
sudo yum install -y python-qrcode-5.3-1.noarch.rpm
fpm -s python -t rpm querystring-parser==1.2.4
sudo yum install -y python-querystring_parser-1.2.4-1.noarch.rpm
fpm -s python -t rpm rb==1.7
sudo yum install -y python-rb-1.7-1.noarch.rpm
fpm -s python -t rpm redis-py-cluster==1.3.4
sudo yum install -y python-redis-py-cluster-1.3.4-1.noarch.rpm
fpm -s python -t rpm redis==2.10.5
sudo yum install -y python-redis-2.10.5-1.noarch.rpm
fpm -s python -t rpm requests-oauthlib==0.3.3
sudo yum install -y python-requests-oauthlib-0.3.3-1.noarch.rpm
fpm -s python -t rpm requests==2.20.1
sudo yum install -y python-requests-2.20.1-1.noarch.rpm
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
fpm -s python -t rpm six==1.10.0
sudo yum install -y python-six-1.10.0-1.noarch.rpm
fpm -s python -t rpm pytest==3.5.1
sudo yum install -y python-pytest-3.5.1-1.noarch.rpm
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
fpm -s python -t rpm unidiff==0.5.5
sudo yum install -y python-unidiff-0.5.5-1.noarch.rpm
fpm -s python -t rpm uwsgi==2.0.18
sudo yum install -y python-uwsgi-2.0.18-1.noarch.rpm

echo "Install nodejs and yarn"
#curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
#sudo yum install -y nodejs
#sudo sed -e '/nodesource-source/,+6d' -i /etc/yum.repos.d/nodesource-el7.repo
#curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo

echo "Build sentry rpm by fpm"
#fpm -s python -t rpm sentry==9.1.2
