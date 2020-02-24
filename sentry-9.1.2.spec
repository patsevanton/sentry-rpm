# Created by pyp2rpm-3.3.3
%global pypi_name sentry

Name:           python-%{pypi_name}
Version:        9.1.2
Release:        1%{?dist}
Summary:        A realtime logging and aggregation server

License:        BSD
URL:            https://sentry.io
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  nodejs
BuildRequires:  yarn

%description
What's Sentry? --Sentry fundamentally is a service that helps you monitor and
fix crashes in realtime. The server is in Python, but it contains a full API
for sending events from any language, in any application.Official Sentry SDKs *
JavaScript < * React-Native < * Python < * Ruby < * PHP < * Go < * Java <

%package -n     python2-%{pypi_name}
Summary:        A realtime logging and aggregation server

Requires:       python2-BeautifulSoup >= 3.2.1
Requires:       python2-Django < 1.7
Requires:       python2-Django >= 1.6.11
Requires:       python2-Pillow <= 4.2.1
Requires:       python2-Pillow >= 3.2.0
Requires:       python2-PyJWT < 1.6.0
Requires:       python2-PyJWT >= 1.5.0
Requires:       python2-PyYAML < 3.12
Requires:       python2-PyYAML >= 3.11
Requires:       python2-batching-kafka-consumer = 0.0.3
Requires:       python2-betamax < 0.9.0
Requires:       python2-betamax >= 0.8.1
Requires:       python2-blist
Requires:       python2-boto3 < 1.4.6
Requires:       python2-boto3 >= 1.4.1
Requires:       python2-botocore < 1.5.71
Requires:       python2-cassandra-driver <= 3.5.0
Requires:       python2-casscache
Requires:       python2-celery < 3.1.19
Requires:       python2-celery >= 3.1.8
Requires:       python2-cffi < 2.0
Requires:       python2-cffi >= 1.11.5
Requires:       python2-click < 7.0
Requires:       python2-click >= 5.0
Requires:       python2-confluent-kafka = 0.11.5
Requires:       python2-cqlsh
Requires:       python2-croniter < 0.4.0
Requires:       python2-croniter >= 0.3.26
Requires:       python2-cssutils < 0.10.0
Requires:       python2-cssutils >= 0.9.9
Requires:       python2-datadog
Requires:       python2-dateutil < 3.0.0
Requires:       python2-dateutil >= 2.0.0
Requires:       python2-django-crispy-forms < 1.5.0
Requires:       python2-django-crispy-forms >= 1.4.0
Requires:       python2-django-jsonfield < 0.9.14
Requires:       python2-django-jsonfield >= 0.9.13
Requires:       python2-django-picklefield < 0.4.0
Requires:       python2-django-picklefield >= 0.3.0
Requires:       python2-django-sudo < 3.0.0
Requires:       python2-django-sudo >= 2.1.0
Requires:       python2-django-templatetag-sugar >= 0.1.0
Requires:       python2-djangorestframework < 2.5.0
Requires:       python2-djangorestframework >= 2.4.8
Requires:       python2-email-reply-parser < 0.3.0
Requires:       python2-email-reply-parser >= 0.2.0
Requires:       python2-enum34 < 1.2.0
Requires:       python2-enum34 >= 1.1.6
Requires:       python2-exam >= 0.5.1
Requires:       python2-freezegun = 0.3.11
Requires:       python2-functools32 < 3.3
Requires:       python2-functools32 >= 3.2.3
Requires:       python2-futures < 4.0.0
Requires:       python2-futures >= 3.2.0
Requires:       python2-google-cloud-bigtable < 0.33.0
Requires:       python2-google-cloud-bigtable >= 0.32.1
Requires:       python2-google-cloud-pubsub < 0.36.0
Requires:       python2-google-cloud-pubsub >= 0.35.4
Requires:       python2-google-cloud-storage < 1.14
Requires:       python2-google-cloud-storage >= 1.13.2
Requires:       python2-hiredis < 0.2.0
Requires:       python2-hiredis >= 0.1.0
Requires:       python2-honcho < 1.1.0
Requires:       python2-honcho >= 1.0.0
Requires:       python2-ipaddress < 1.1.0
Requires:       python2-ipaddress >= 1.0.16
Requires:       python2-jsonschema = 2.6.0
Requires:       python2-kombu = 3.0.35
Requires:       python2-loremipsum < 1.1.0
Requires:       python2-loremipsum >= 1.0.5
Requires:       python2-lxml >= 3.4.1
Requires:       python2-maxminddb = 1.4.1
Requires:       python2-memcached < 2.0.0
Requires:       python2-memcached >= 1.53
Requires:       python2-mistune < 0.9
Requires:       python2-mistune > 0.7
Requires:       python2-mmh3 < 2.4
Requires:       python2-mmh3 >= 2.3.1
Requires:       python2-mock = 2.0.0
Requires:       python2-msgpack < 0.5.0
Requires:       python2-msgpack < 0.7.0
Requires:       python2-msgpack >= 0.6.1
Requires:       python2-oauth2 >= 1.5.167
Requires:       python2-openid >= 2.2
Requires:       python2-parsimonious = 0.8.0
Requires:       python2-percy >= 1.1.2
Requires:       python2-petname < 2.1
Requires:       python2-petname >= 2.0
Requires:       python2-progressbar2 < 3.11
Requires:       python2-progressbar2 >= 3.10
Requires:       python2-psycopg2-binary < 2.8.0
Requires:       python2-psycopg2-binary >= 2.6.0
Requires:       python2-pytest < 3.6.0
Requires:       python2-pytest >= 3.5.0
Requires:       python2-pytest-cov < 2.6.0
Requires:       python2-pytest-cov >= 2.5.1
Requires:       python2-pytest-django < 2.10.0
Requires:       python2-pytest-django >= 2.9.1
Requires:       python2-pytest-html < 1.10.0
Requires:       python2-pytest-html >= 1.9.0
Requires:       python2-pytest-timeout = 1.2.1
Requires:       python2-pytest-xdist < 1.19.0
Requires:       python2-pytest-xdist >= 1.18.0
Requires:       python2-qrcode < 6.0.0
Requires:       python2-qrcode >= 5.2.2
Requires:       python2-querystring-parser < 2.0.0
Requires:       python2-querystring-parser >= 1.2.3
Requires:       python2-rb < 2.0.0
Requires:       python2-rb >= 1.7.0
Requires:       python2-redis < 2.10.6
Requires:       python2-redis >= 2.10.3
Requires:       python2-redis-py-cluster = 1.3.4
Requires:       python2-requests < 2.21.0
Requires:       python2-requests >= 2.20.0
Requires:       python2-requests-oauthlib = 0.3.3
Requires:       python2-responses < 0.9.0
Requires:       python2-responses >= 0.8.1
Requires:       python2-saml < 1.5
Requires:       python2-saml >= 1.4.0
Requires:       python2-selenium = 3.141.0
Requires:       python2-semaphore < 0.5.0
Requires:       python2-semaphore >= 0.4.21
Requires:       python2-sentry-sdk >= 0.7.0
Requires:       python2-setproctitle < 1.2.0
Requires:       python2-setproctitle >= 1.1.7
Requires:       python2-setuptools
Requires:       python2-simplejson < 3.9.0
Requires:       python2-simplejson >= 3.2.0
Requires:       python2-six < 1.11.0
Requires:       python2-six >= 1.10.0
Requires:       python2-sqlparse < 0.2.0
Requires:       python2-sqlparse = 0.2.4
Requires:       python2-sqlparse >= 0.1.16
Requires:       python2-statsd < 3.2.0
Requires:       python2-statsd >= 3.1.0
Requires:       python2-strict-rfc3339 >= 0.7
Requires:       python2-structlog = 16.1.0
Requires:       python2-symbolic < 7.0.0
Requires:       python2-symbolic >= 6.0.4
Requires:       python2-toronado < 0.1.0
Requires:       python2-toronado >= 0.0.11
Requires:       python2-u2flib-server < 4.1.0
Requires:       python2-u2flib-server >= 4.0.1
Requires:       python2-ua-parser < 0.8.0
Requires:       python2-ua-parser >= 0.6.1
Requires:       python2-unidiff >= 0.5.4
Requires:       python2-urllib3 = 1.24.2
Requires:       python2-uwsgi < 2.1.0
Requires:       python2-uwsgi > 2.0.0
%description -n python2-%{pypi_name}
What's Sentry? --Sentry fundamentally is a service that helps you monitor and
fix crashes in realtime. The server is in Python, but it contains a full API
for sending events from any language, in any application.Official Sentry SDKs *
JavaScript < * React-Native < * Python < * Ruby < * PHP < * Go < * Java <


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pypi_name}
%doc src/sentry/pipeline/README.md src/sentry/logging/README.rst src/sentry/nodestore/README.rst README.rst
%{_bindir}/sentry
%{python2_sitelib}/bitfield
%{python2_sitelib}/debug_toolbar
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/social_auth
%{python2_sitelib}/south
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info

%changelog
* Mon Feb 24 2020 Cloud User - 9.1.2-1
- Initial package.
