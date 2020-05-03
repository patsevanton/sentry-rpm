# Created by pyp2rpm-3.3.3
%global pypi_name sentry-ldap-auth

Name:           python-%{pypi_name}
Version:        2.8.1
Release:        1%{?dist}
Summary:        A Sentry extension to add an LDAP server as an authentication source

License:        Apache-2.0
URL:            http://github.com/banno/getsentry-ldap-auth
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description
 sentry-ldap-authA Django custom authentication backend for [Sentry]( This
module extends the functionality of [django-auth-ldap]( with Sentry specific
features. Features * Users created by this backend are managed users. Managed
fields are not editable through the Sentry account page. * Users may be auto-
added to an Organization upon creation. Prerequisites Versions 2.0 and newer
require...

%package -n     python2-%{pypi_name}
Summary:        A Sentry extension to add an LDAP server as an authentication source

Requires:       python2-django-auth-ldap = 1.2.17
Requires:       python2-sentry >= 8.0.0
%description -n python2-%{pypi_name}
 sentry-ldap-authA Django custom authentication backend for [Sentry]( This
module extends the functionality of [django-auth-ldap]( with Sentry specific
features. Features * Users created by this backend are managed users. Managed
fields are not editable through the Sentry account page. * Users may be auto-
added to an Organization upon creation. Prerequisites Versions 2.0 and newer
require...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pypi_name}
%doc README.md
%{python2_sitelib}/sentry_ldap_auth
%{python2_sitelib}/sentry_ldap_auth-%{version}-py%{python2_version}.egg-info

%changelog
* Sun May 03 2020 Cloud User - 2.8.1-1
- Initial package.
