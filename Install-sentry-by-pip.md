# Установка sentry через pip на Centos 7 для проверки списка зависимостей в vagrant

```
sudo yum install -y epel-release mc gcc gcc-c++ python-devel
sudo yum install -y python2-pip ca-certificates
reboot
sudo pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org requests==2.20.1 -U --ignore-installed
Successfully installed certifi-2019.11.28 chardet-2.2.1 idna-2.7 requests-2.20.1 urllib3-1.24.3

sudo pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org --upgrade pip
Successfully installed pip-20.0.2

sudo pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org PyYAML==3.11 -U --ignore-installed
Successfully installed PyYAML-3.11

```
sudo pip install --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org sentry==9.1.2

Collecting sentry==9.1.2
  Downloading sentry-9.1.2-py27-none-any.whl (27.2 MB)
     |████████████████████████████████| 27.2 MB 6.6 MB/s 
Collecting structlog==16.1.0
  Downloading structlog-16.1.0-py2.py3-none-any.whl (28 kB)
Collecting toronado<0.1.0,>=0.0.11
  Downloading toronado-0.0.11.tar.gz (4.6 kB)
Collecting PyJWT<1.6.0,>=1.5.0
  Downloading PyJWT-1.5.3-py2.py3-none-any.whl (17 kB)
Collecting python-memcached<2.0.0,>=1.53
  Downloading python_memcached-1.59-py2.py3-none-any.whl (16 kB)
Collecting djangorestframework<2.5.0,>=2.4.8
  Downloading djangorestframework-2.4.8-py2.py3-none-any.whl (193 kB)
     |████████████████████████████████| 193 kB 21.9 MB/s 
Collecting exam>=0.5.1
  Downloading exam-0.10.6.tar.gz (15 kB)
Collecting strict-rfc3339>=0.7
  Downloading strict-rfc3339-0.7.tar.gz (17 kB)
Collecting unidiff>=0.5.4
  Downloading unidiff-0.5.5-py2.py3-none-any.whl (14 kB)
Collecting kombu==3.0.35
  Downloading kombu-3.0.35-py2.py3-none-any.whl (240 kB)
     |████████████████████████████████| 240 kB 17.1 MB/s 
Collecting pytest-html<1.10.0,>=1.9.0
  Downloading pytest_html-1.9.0-py2.py3-none-any.whl (12 kB)
Collecting sqlparse<0.2.0,>=0.1.16
  Downloading sqlparse-0.1.19.tar.gz (58 kB)
     |████████████████████████████████| 58 kB 14.7 MB/s 
Collecting mock==2.0.0
  Downloading mock-2.0.0-py2.py3-none-any.whl (56 kB)
     |████████████████████████████████| 56 kB 19.8 MB/s 
Collecting pytest<3.6.0,>=3.5.0
  Downloading pytest-3.5.1-py2.py3-none-any.whl (192 kB)
     |████████████████████████████████| 192 kB 20.5 MB/s 
Collecting python-u2flib-server<4.1.0,>=4.0.1
  Downloading python-u2flib-server-4.0.1.tar.gz (35 kB)
Collecting celery<3.1.19,>=3.1.8
  Downloading celery-3.1.18-py2.py3-none-any.whl (515 kB)
     |████████████████████████████████| 515 kB 16.9 MB/s 
Collecting petname<2.1,>=2.0
  Downloading petname-2.0.tar.gz (8.1 kB)
Collecting email-reply-parser<0.3.0,>=0.2.0
  Downloading email_reply_parser-0.2.0.tar.gz (3.1 kB)
Collecting django-picklefield<0.4.0,>=0.3.0
  Downloading django_picklefield-0.3.2-py2.py3-none-any.whl (13 kB)
Collecting percy>=1.1.2
  Downloading percy-2.0.2-py2.py3-none-any.whl (12 kB)
Collecting django-templatetag-sugar>=0.1.0
  Downloading django_templatetag_sugar-1.0-py2.py3-none-any.whl (5.2 kB)
Collecting Django<1.7,>=1.6.11
  Downloading Django-1.6.11-py2.py3-none-any.whl (6.7 MB)
     |████████████████████████████████| 6.7 MB 5.1 MB/s 
Collecting six<1.11.0,>=1.10.0
  Downloading six-1.10.0-py2.py3-none-any.whl (10 kB)
Collecting enum34<1.2.0,>=1.1.6
  Downloading enum34-1.1.9-py2-none-any.whl (11 kB)
Collecting loremipsum<1.1.0,>=1.0.5
  Downloading loremipsum-1.0.5.tar.gz (11 kB)
Collecting functools32<3.3,>=3.2.3
  Downloading functools32-3.2.3-2.tar.gz (31 kB)
Collecting parsimonious==0.8.0
  Downloading parsimonious-0.8.0.tar.gz (38 kB)
Collecting hiredis<0.2.0,>=0.1.0
  Downloading hiredis-0.1.6.tar.gz (45 kB)
     |████████████████████████████████| 45 kB 17.1 MB/s 
Collecting python-openid>=2.2
  Downloading python-openid-2.2.5.tar.gz (301 kB)
     |████████████████████████████████| 301 kB 21.3 MB/s 
Collecting urllib3==1.24.2
  Downloading urllib3-1.24.2-py2.py3-none-any.whl (131 kB)
     |████████████████████████████████| 131 kB 14.1 MB/s 
Collecting requests-oauthlib==0.3.3
  Downloading requests-oauthlib-0.3.3.tar.gz (9.6 kB)
Collecting jsonschema==2.6.0
  Downloading jsonschema-2.6.0-py2.py3-none-any.whl (39 kB)
Collecting sentry-sdk>=0.7.0
  Downloading sentry_sdk-0.14.1-py2.py3-none-any.whl (93 kB)
     |████████████████████████████████| 93 kB 5.6 MB/s 
Collecting click<7.0,>=5.0
  Downloading click-6.7-py2.py3-none-any.whl (71 kB)
     |████████████████████████████████| 71 kB 13.6 MB/s 
Collecting ua-parser<0.8.0,>=0.6.1
  Downloading ua_parser-0.7.3-py2.py3-none-any.whl (33 kB)
Collecting progressbar2<3.11,>=3.10
  Downloading progressbar2-3.10.1-py2.py3-none-any.whl (20 kB)
Collecting django-crispy-forms<1.5.0,>=1.4.0
  Downloading django-crispy-forms-1.4.0.tar.gz (47 kB)
     |████████████████████████████████| 47 kB 28.6 MB/s 
Collecting selenium==3.141.0
  Downloading selenium-3.141.0-py2.py3-none-any.whl (904 kB)
     |████████████████████████████████| 904 kB 12.0 MB/s 
Collecting oauth2>=1.5.167
  Downloading oauth2-1.9.0.post1-py2.py3-none-any.whl (25 kB)
Collecting setproctitle<1.2.0,>=1.1.7
  Downloading setproctitle-1.1.10.tar.gz (24 kB)
Collecting boto3<1.4.6,>=1.4.1
  Downloading boto3-1.4.5-py2.py3-none-any.whl (128 kB)
     |████████████████████████████████| 128 kB 14.3 MB/s 
Collecting futures<4.0.0,>=3.2.0
  Downloading futures-3.3.0-py2-none-any.whl (16 kB)
Requirement already satisfied: requests[security]<2.21.0,>=2.20.0 in /usr/lib/python2.7/site-packages (from sentry==9.1.2) (2.20.1)
Collecting honcho<1.1.0,>=1.0.0
  Downloading honcho-1.0.1-py2.py3-none-any.whl (21 kB)
Collecting symbolic<7.0.0,>=6.0.4
  Downloading symbolic-6.1.4-py2.py3-none-manylinux1_x86_64.whl (11.5 MB)
     |████████████████████████████████| 11.5 MB 7.7 MB/s 
Collecting croniter<0.4.0,>=0.3.26
  Downloading croniter-0.3.31-py2.py3-none-any.whl (16 kB)
Collecting Pillow<=4.2.1,>=3.2.0
  Downloading Pillow-4.2.1-cp27-cp27mu-manylinux1_x86_64.whl (5.8 MB)
     |████████████████████████████████| 5.8 MB 11.5 MB/s 
Collecting msgpack<0.7.0,>=0.6.1
  Downloading msgpack-0.6.2-cp27-cp27mu-manylinux1_x86_64.whl (232 kB)
     |████████████████████████████████| 232 kB 11.6 MB/s 
Collecting qrcode<6.0.0,>=5.2.2
  Downloading qrcode-5.3-py2.py3-none-any.whl (31 kB)
Collecting mistune<0.9,>0.7
  Downloading mistune-0.8.4-py2.py3-none-any.whl (16 kB)
Collecting redis<2.10.6,>=2.10.3
  Downloading redis-2.10.5-py2.py3-none-any.whl (60 kB)
     |████████████████████████████████| 60 kB 13.5 MB/s 
Collecting psycopg2-binary<2.8.0,>=2.6.0
  Downloading psycopg2_binary-2.7.7-cp27-cp27mu-manylinux1_x86_64.whl (2.7 MB)
     |████████████████████████████████| 2.7 MB 16.1 MB/s 
Collecting uwsgi<2.1.0,>2.0.0
  Downloading uwsgi-2.0.18.tar.gz (801 kB)
     |████████████████████████████████| 801 kB 12.6 MB/s 
Collecting cffi<2.0,>=1.11.5
  Downloading cffi-1.14.0-cp27-cp27mu-manylinux1_x86_64.whl (387 kB)
     |████████████████████████████████| 387 kB 9.9 MB/s 
Collecting BeautifulSoup>=3.2.1
  Downloading BeautifulSoup-3.2.2-py2-none-any.whl (32 kB)
Collecting botocore<1.5.71
  Downloading botocore-1.5.70-py2.py3-none-any.whl (3.5 MB)
     |████████████████████████████████| 3.5 MB 5.2 MB/s 
Collecting pytest-django<2.10.0,>=2.9.1
  Downloading pytest_django-2.9.1-py2.py3-none-any.whl (18 kB)
Collecting python-dateutil<3.0.0,>=2.0.0
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 5.6 MB/s 
Collecting rb<2.0.0,>=1.7.0
  Downloading rb-1.7-py2-none-any.whl (22 kB)
Collecting statsd<3.2.0,>=3.1.0
  Downloading statsd-3.1-py2.py3-none-any.whl (11 kB)
Collecting django-sudo<3.0.0,>=2.1.0
  Downloading django_sudo-2.1.0-py2.py3-none-any.whl (11 kB)
Collecting lxml>=3.4.1
  Downloading lxml-4.5.0-cp27-cp27mu-manylinux1_x86_64.whl (5.7 MB)
     |████████████████████████████████| 5.7 MB 4.9 MB/s 
Collecting redis-py-cluster==1.3.4
  Downloading redis_py_cluster-1.3.4-py2.py3-none-any.whl (39 kB)
Collecting querystring-parser<2.0.0,>=1.2.3
  Downloading querystring_parser-1.2.4.tar.gz (5.5 kB)
Collecting cssutils<0.10.0,>=0.9.9
  Downloading cssutils-0.9.10.zip (430 kB)
     |████████████████████████████████| 430 kB 21.2 MB/s 
Requirement already satisfied: PyYAML<3.12,>=3.11 in /usr/lib64/python2.7/site-packages (from sentry==9.1.2) (3.11)
Collecting simplejson<3.9.0,>=3.2.0
  Downloading simplejson-3.8.2.tar.gz (76 kB)
     |████████████████████████████████| 76 kB 18.3 MB/s 
Collecting django-jsonfield<0.9.14,>=0.9.13
  Downloading django-jsonfield-0.9.13.tar.gz (11 kB)
Requirement already satisfied: ipaddress<1.1.0,>=1.0.16 in /usr/lib/python2.7/site-packages (from sentry==9.1.2) (1.0.16)
Collecting mmh3<2.4,>=2.3.1
  Downloading mmh3-2.3.1.tar.gz (6.1 kB)
Collecting semaphore<0.5.0,>=0.4.21
  Downloading semaphore-0.4.65-py2.py3-none-manylinux1_x86_64.whl (19.7 MB)
     |████████████████████████████████| 19.7 MB 9.0 MB/s 
Collecting cssselect
  Downloading cssselect-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting amqp<2.0,>=1.4.9
  Downloading amqp-1.4.9-py2.py3-none-any.whl (51 kB)
     |████████████████████████████████| 51 kB 4.4 MB/s 
Collecting anyjson>=0.3.3
  Downloading anyjson-0.3.3.tar.gz (8.3 kB)
Collecting pbr>=0.11
  Downloading pbr-5.4.4-py2.py3-none-any.whl (110 kB)
     |████████████████████████████████| 110 kB 39.3 MB/s 
Collecting funcsigs>=1; python_version < "3.3"
  Downloading funcsigs-1.0.2-py2.py3-none-any.whl (17 kB)
Collecting pluggy<0.7,>=0.5
  Downloading pluggy-0.6.0-py2-none-any.whl (11 kB)
Collecting py>=1.5.0
  Downloading py-1.8.1-py2.py3-none-any.whl (83 kB)
     |████████████████████████████████| 83 kB 29.9 MB/s 
Collecting attrs>=17.4.0
  Downloading attrs-19.3.0-py2.py3-none-any.whl (39 kB)
Collecting more-itertools>=4.0.0
  Downloading more_itertools-5.0.0-py2-none-any.whl (52 kB)
     |████████████████████████████████| 52 kB 14.7 MB/s 
Requirement already satisfied: setuptools in /usr/lib/python2.7/site-packages (from pytest<3.6.0,>=3.5.0->sentry==9.1.2) (0.9.8)
Collecting cryptography>=1.2
  Downloading cryptography-2.8-cp27-cp27mu-manylinux2010_x86_64.whl (2.3 MB)
     |████████████████████████████████| 2.3 MB 13.5 MB/s 
Collecting billiard<3.4,>=3.3.0.20
  Downloading billiard-3.3.0.23.tar.gz (151 kB)
     |████████████████████████████████| 151 kB 14.4 MB/s 
Collecting pytz>dev
  Downloading pytz-2019.3-py2.py3-none-any.whl (509 kB)
     |████████████████████████████████| 509 kB 15.9 MB/s 
Collecting oauthlib>=0.4.2
  Downloading oauthlib-3.1.0-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB 14.0 MB/s 
Requirement already satisfied: certifi in /usr/lib/python2.7/site-packages (from sentry-sdk>=0.7.0->sentry==9.1.2) (2019.11.28)
Collecting python-utils>=2.0.0
  Downloading python_utils-2.3.0-py2.py3-none-any.whl (12 kB)
Collecting httplib2
  Downloading httplib2-0.17.0.tar.gz (220 kB)
     |████████████████████████████████| 220 kB 17.5 MB/s 
Collecting jmespath<1.0.0,>=0.7.1
  Downloading jmespath-0.9.5-py2.py3-none-any.whl (24 kB)
Collecting s3transfer<0.2.0,>=0.1.10
  Downloading s3transfer-0.1.13-py2.py3-none-any.whl (59 kB)
     |████████████████████████████████| 59 kB 29.0 MB/s 
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/lib/python2.7/site-packages (from requests[security]<2.21.0,>=2.20.0->sentry==9.1.2) (3.0.4)
Requirement already satisfied: idna<2.8,>=2.5 in /usr/lib/python2.7/site-packages (from requests[security]<2.21.0,>=2.20.0->sentry==9.1.2) (2.7)
Collecting pyOpenSSL>=0.14; extra == "security"
  Downloading pyOpenSSL-19.1.0-py2.py3-none-any.whl (53 kB)
     |████████████████████████████████| 53 kB 12.3 MB/s 
Collecting milksnake>=0.1.2
  Downloading milksnake-0.1.5-py2.py3-none-any.whl (9.6 kB)
Collecting olefile
  Downloading olefile-0.46.zip (112 kB)
     |████████████████████████████████| 112 kB 19.4 MB/s 
Collecting pycparser
  Downloading pycparser-2.19.tar.gz (158 kB)
     |████████████████████████████████| 158 kB 16.8 MB/s 
Collecting docutils>=0.10
  Downloading docutils-0.16-py2.py3-none-any.whl (548 kB)
     |████████████████████████████████| 548 kB 19.4 MB/s 
Installing collected packages: six, structlog, cssselect, cssutils, lxml, toronado, PyJWT, python-memcached, djangorestframework, pbr, funcsigs, mock, exam, strict-rfc3339, unidiff, amqp, anyjson, kombu, pluggy, py, attrs, more-itertools, pytest, pytest-html, sqlparse, pycparser, cffi, enum34, cryptography, python-u2flib-server, billiard, pytz, celery, petname, email-reply-parser, django-picklefield, percy, django-templatetag-sugar, Django, loremipsum, functools32, parsimonious, hiredis, python-openid, urllib3, oauthlib, requests-oauthlib, jsonschema, sentry-sdk, click, ua-parser, python-utils, progressbar2, django-crispy-forms, selenium, httplib2, oauth2, setproctitle, jmespath, python-dateutil, docutils, botocore, futures, s3transfer, boto3, honcho, milksnake, symbolic, croniter, olefile, Pillow, msgpack, qrcode, mistune, redis, psycopg2-binary, uwsgi, BeautifulSoup, pytest-django, rb, statsd, django-sudo, redis-py-cluster, querystring-parser, simplejson, django-jsonfield, mmh3, semaphore, sentry, pyOpenSSL
    Running setup.py install for cssutils ... done
    Running setup.py install for toronado ... done
    Running setup.py install for exam ... done
    Running setup.py install for strict-rfc3339 ... done
    Running setup.py install for anyjson ... done
    Running setup.py install for sqlparse ... done
    Running setup.py install for pycparser ... done
    Running setup.py install for python-u2flib-server ... done
    Running setup.py install for billiard ... done
    Running setup.py install for petname ... done
    Running setup.py install for email-reply-parser ... done
    Running setup.py install for loremipsum ... done
    Running setup.py install for functools32 ... done
    Running setup.py install for parsimonious ... done
    Running setup.py install for hiredis ... done
    Running setup.py install for python-openid ... done
  Attempting uninstall: urllib3
    Found existing installation: urllib3 1.24.3
    Uninstalling urllib3-1.24.3:
      Successfully uninstalled urllib3-1.24.3
    Running setup.py install for requests-oauthlib ... done
    Running setup.py install for django-crispy-forms ... done
    Running setup.py install for httplib2 ... done
    Running setup.py install for setproctitle ... done
    Running setup.py install for olefile ... done
    Running setup.py install for uwsgi ... done
    Running setup.py install for querystring-parser ... done
    Running setup.py install for simplejson ... done
    Running setup.py install for django-jsonfield ... done
    Running setup.py install for mmh3 ... done
Successfully installed BeautifulSoup-3.2.2 Django-1.6.11 Pillow-4.2.1 PyJWT-1.5.3 amqp-1.4.9 anyjson-0.3.3 attrs-19.3.0 billiard-3.3.0.23 boto3-1.4.5 botocore-1.5.70 celery-3.1.18 cffi-1.14.0 click-6.7 croniter-0.3.31 cryptography-2.8 cssselect-1.1.0 cssutils-0.9.10 django-crispy-forms-1.4.0 django-jsonfield-0.9.13 django-picklefield-0.3.2 django-sudo-2.1.0 django-templatetag-sugar-1.0 djangorestframework-2.4.8 docutils-0.16 email-reply-parser-0.2.0 enum34-1.1.9 exam-0.10.6 funcsigs-1.0.2 functools32-3.2.3.post2 futures-3.3.0 hiredis-0.1.6 honcho-1.0.1 httplib2-0.17.0 jmespath-0.9.5 jsonschema-2.6.0 kombu-3.0.35 loremipsum-1.0.5 lxml-4.5.0 milksnake-0.1.5 mistune-0.8.4 mmh3-2.3.1 mock-2.0.0 more-itertools-5.0.0 msgpack-0.6.2 oauth2-1.9.0.post1 oauthlib-3.1.0 olefile-0.46 parsimonious-0.8.0 pbr-5.4.4 percy-2.0.2 petname-2.0 pluggy-0.6.0 progressbar2-3.10.1 psycopg2-binary-2.7.7 py-1.8.1 pyOpenSSL-19.1.0 pycparser-2.19 pytest-3.5.1 pytest-django-2.9.1 pytest-html-1.9.0 python-dateutil-2.8.1 python-memcached-1.59 python-openid-2.2.5 python-u2flib-server-4.0.1 python-utils-2.3.0 pytz-2019.3 qrcode-5.3 querystring-parser-1.2.4 rb-1.7 redis-2.10.5 redis-py-cluster-1.3.4 requests-oauthlib-0.3.3 s3transfer-0.1.13 selenium-3.141.0 semaphore-0.4.65 sentry-9.1.2 sentry-sdk-0.14.1 setproctitle-1.1.10 simplejson-3.8.2 six-1.10.0 sqlparse-0.1.19 statsd-3.1 strict-rfc3339-0.7 structlog-16.1.0 symbolic-6.1.4 toronado-0.0.11 ua-parser-0.7.3 unidiff-0.5.5 urllib3-1.24.2 uwsgi-2.0.18
```
`
