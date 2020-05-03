# Created by pyp2rpm-3.3.3
%global pypi_name django-auth-ldap

Name:           python-%{pypi_name}
Version:        1.2.17
Release:        1%{?dist}
Summary:        Django LDAP authentication backend

License:        BSD
URL:            https://bitbucket.org/illocution/django-auth-ldap
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-django16
BuildRequires:  python2-ldap >= 2.0
BuildRequires:  python2-setuptools >= 0.6c11

%description
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.This version is supported on Python 2.7, 3.3, 3.4, 3.5,
and 3.6; and Django > 1.5. Under Python 2, it requires python-ldap < > 2.0;
under Python...

%package -n     python2-%{pypi_name}
Summary:        Django LDAP authentication backend

Requires:       python2-django16
Requires:       python2-ldap >= 2.0
%description -n python2-%{pypi_name}
This is a Django authentication backend that authenticates against an LDAP
service. Configuration can be as simple as a single distinguished name
template, but there are many rich configuration options for working with users,
groups, and permissions.This version is supported on Python 2.7, 3.3, 3.4, 3.5,
and 3.6; and Django > 1.5. Under Python 2, it requires python-ldap < > 2.0;
under Python...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pypi_name}
%{python2_sitelib}/django_auth_ldap
%{python2_sitelib}/django_auth_ldap-%{version}-py%{python2_version}.egg-info

%changelog
* Sun May 03 2020 Cloud User - 1.2.17-1
- Initial package.
