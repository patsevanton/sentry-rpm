# Created by pyp2rpm-3.3.3
%global pypi_name sentry

Name:           python-%{pypi_name}
Version:        9.1.2
Release:        1%{?dist}
Summary:        A realtime logging and aggregation server

License:        BSD
URL:            https://sentry.io
Source0:        sentry-cron.service
Source1:        sentry-web.service
Source2:        sentry-worker.service
Source3:        config.yml
Source4:        sentry.conf.py
BuildArch:      noarch
Requires(pre):  shadow-utils
BuildRequires:  python2-devel
BuildRequires:  nodejs >= 8
BuildRequires:  yarn

# Use systemd for fedora >= 18, rhel >=7, SUSE >= 12 SP1 and openSUSE >= 42.1
%define use_systemd (0%{?fedora} && 0%{?fedora} >= 18) || (0%{?rhel} && 0%{?rhel} >= 7) || (!0%{?is_opensuse} && 0%{?suse_version} >=1210) || (0%{?is_opensuse} && 0%{?sle_version} >= 120100)

Requires:       memcached
Requires:       redis
Requires:       python-BeautifulSoup >= 3.2.1
Requires:       python-boto3 < 1.4.6
Requires:       python-boto3 >= 1.4.1
Requires:       python-cffi < 2.0
Requires:       python-cffi >= 1.11.5
Requires:       python-croniter < 0.4.0
Requires:       python-croniter >= 0.3.26
Requires:       python-ipaddress < 1.1.0
Requires:       python-ipaddress >= 1.0.16
Requires:       python-lxml >= 3.4.1
Requires:       python-memcached < 2.0.0
Requires:       python-memcached >= 1.53
Requires:       python-mistune < 0.9
Requires:       python-mistune > 0.7
Requires:       python-oauth2 >= 1.5.167
Requires:       python-openid >= 2.2
Requires:       python-pillow <= 4.2.1
Requires:       python-pillow >= 3.2.0
Requires:       python-qrcode < 6.0.0
Requires:       python-qrcode >= 5.2.2
Requires:       python-setproctitle < 1.2.0
Requires:       python-setproctitle >= 1.1.7
Requires:       python-setuptools
Requires:       python-urllib3 = 1.24.2
Requires:       python-botocore < 1.5.71
Requires:       python-celery < 3.1.19
Requires:       python-celery >= 3.1.8
Requires:       python2-click < 7.0
Requires:       python2-click >= 5.0
Requires:       python-cssutils < 0.10.0
Requires:       python-cssutils >= 0.9.9
Requires:       python-dateutil < 3.0.0
Requires:       python-dateutil >= 2.0.0
Requires:       python2-django16 < 1.7
Requires:       python2-django16 >= 1.6.11
Requires:       python-django-crispy-forms < 1.5.0
Requires:       python-django-crispy-forms >= 1.4.0
Requires:       python-django-jsonfield < 0.9.14
Requires:       python-django-jsonfield >= 0.9.13
Requires:       python-django-picklefield < 0.4.0
Requires:       python-django-picklefield >= 0.3.0
Requires:       python-django-sudo < 3.0.0
Requires:       python-django-sudo >= 2.1.0
Requires:       python-django-templatetag-sugar >= 0.1.0
Requires:       python-djangorestframework < 2.5.0
Requires:       python-djangorestframework >= 2.4.8
Requires:       python-email_reply_parser < 0.3.0
Requires:       python-email_reply_parser >= 0.2.0
Requires:       python-enum34 < 1.2.0
Requires:       python-enum34 >= 1.1.6
Requires:       python-functools32 < 3.3
Requires:       python-functools32 >= 3.2.3
Requires:       python-futures < 4.0.0
Requires:       python-futures >= 3.2.0
Requires:       python-hiredis < 0.2.0
Requires:       python-hiredis >= 0.1.0
Requires:       python-honcho < 1.1.0
Requires:       python-honcho >= 1.0.0
Requires:       python-jsonschema = 2.6.0
Requires:       python-kombu = 3.0.35
Requires:       python-loremipsum < 1.1.0
Requires:       python-loremipsum >= 1.0.5
Requires:       python-mmh3 < 2.4
Requires:       python-mmh3 >= 2.3.1
Requires:       python-mock = 2.0.0
Requires:       python-msgpack < 0.7.0
Requires:       python-msgpack >= 0.6.1
Requires:       python-parsimonious = 0.8.0
Requires:       python-percy >= 1.1.2
Requires:       python-petname < 2.1
Requires:       python-petname >= 2.0
Requires:       python-progressbar2 < 3.11
Requires:       python-progressbar2 >= 3.10
Requires:       python-psycopg2-binary < 2.8.0
Requires:       python-psycopg2-binary >= 2.6.0
Requires:       python-jwt < 1.6.0
Requires:       python-jwt >= 1.5.0
Requires:       python-pytest < 3.6.0
Requires:       python-pytest >= 3.5.0
Requires:       python-pytest-django < 2.10.0
Requires:       python-pytest-django >= 2.9.1
Requires:       python-pytest-html < 1.10.0
Requires:       python-pytest-html >= 1.9.0
Requires:       python-querystring_parser < 2.0.0
Requires:       python-querystring_parser >= 1.2.3
Requires:       python-rb < 2.0.0
Requires:       python-rb >= 1.7
Requires:       python-redis < 2.10.6
Requires:       python-redis >= 2.10.3
Requires:       python-redis-py-cluster = 1.3.4
Requires:       python-requests < 2.21.0
Requires:       python-requests >= 2.20.0
Requires:       python-requests-oauthlib = 0.3.3
Requires:       python-selenium = 3.141.0
Requires:       python-semaphore < 0.5.0
Requires:       python-semaphore >= 0.4.21
Requires:       python-sentry-sdk >= 0.7.0
Requires:       python-simplejson < 3.9.0
Requires:       python-simplejson >= 3.2.0
Requires:       python-six < 1.11.0
Requires:       python-six >= 1.10.0
Requires:       python-statsd < 3.2.0
Requires:       python-statsd >= 3.1
Requires:       python-strict-rfc3339 >= 0.7
Requires:       python-structlog = 16.1.0
Requires:       python-symbolic < 7.0.0
Requires:       python-symbolic >= 6.0.4
Requires:       python-toronado < 0.1.0
Requires:       python-toronado >= 0.0.11
Requires:       python-u2flib-server < 4.1.0
Requires:       python-u2flib-server >= 4.0.1
Requires:       python-ua-parser < 0.8.0
Requires:       python-ua-parser >= 0.6.1
Requires:       python2-unidiff >= 0.5.4
Requires:       python-uwsgi < 2.1.0
Requires:       python-uwsgi > 2.0.0
Requires:       PyYAML < 3.12
Requires:       PyYAML >= 3.11

%description
What's Sentry? --Sentry fundamentally is a service that helps you monitor and
fix crashes in realtime. The server is in Python, but it contains a full API
for sending events from any language, in any application.Official Sentry SDKs *
JavaScript < * React-Native < * Python < * Ruby < * PHP < * Go < * Java <

%prep
git clone https://github.com/getsentry/sentry.git
cd sentry
git checkout releases/9.1.x

%build
cd sentry
%{__python2} setup.py build

%install
cd sentry
%{__python2} setup.py install --skip-build --root %{buildroot}
%{__install} -m 0755 -d %{buildroot}/home/sentry
%{__install} -m 0755 -d %{buildroot}/etc/sentry
cp %{SOURCE3} %{buildroot}/etc/sentry
cp %{SOURCE4} %{buildroot}/etc/sentry
%if %{use_systemd}
%{__mkdir} -p %{buildroot}%{_unitdir}
%{__install} -m644 %{SOURCE0} %{buildroot}%{_unitdir}/
%{__install} -m644 %{SOURCE1} %{buildroot}%{_unitdir}/
%{__install} -m644 %{SOURCE2} %{buildroot}%{_unitdir}/
%endif

%pre
/usr/bin/getent group sentry > /dev/null || /usr/sbin/groupadd -r sentry
/usr/bin/getent passwd sentry > /dev/null || /usr/sbin/useradd -r -d /home/sentry -s /bin/bash -g sentry sentry

%post
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%preun
%if %use_systemd
/usr/bin/systemctl stop sentry-web
/usr/bin/systemctl stop sentry-worker
/usr/bin/systemctl stop sentry-cron
%endif

%postun
%if %use_systemd
/usr/bin/systemctl daemon-reload
%endif

%files
#%doc src/sentry/pipeline/README.md src/sentry/logging/README.rst src/sentry/nodestore/README.rst README.rst
%{_bindir}/sentry
/etc/sentry
%dir %attr(0775, sentry, sentry) /home/sentry
%{python2_sitelib}/bitfield
%{python2_sitelib}/debug_toolbar
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/social_auth
%{python2_sitelib}/south
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%if %{use_systemd}
%{_unitdir}/sentry-cron.service
%{_unitdir}/sentry-web.service
%{_unitdir}/sentry-worker.service
%endif
