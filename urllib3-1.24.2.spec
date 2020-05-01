# Created by pyp2rpm-3.3.3
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        1.24.2
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/u/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildConflicts: python2-pysocks = 1.5.7
BuildRequires:  python2-pysocks < 2.0
BuildRequires:  python2-pysocks >= 1.5.6
BuildRequires:  python2-certifi
BuildRequires:  python-cryptography >= 1.3.4
BuildRequires:  python-idna >= 2.0.0
BuildRequires:  python-ipaddress
BuildRequires:  python-mock
BuildRequires:  python-pyopenssl >= 0.14
BuildRequires:  python2-pytest
BuildRequires:  python-setuptools
BuildRequires:  python-tornado

%description
 :target:

Conflicts:      python2-pysocks = 1.5.7
Requires:       python2-pysocks < 2.0
Requires:       python2-pysocks >= 1.5.6
Requires:       python2-certifi
Requires:       python-cryptography >= 1.3.4
Requires:       python-idna >= 2.0.0
Requires:       python-ipaddress
Requires:       python-pyopenssl >= 0.14

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
rm -rf %{buildroot}/%{python2_sitelib}/urllib3/packages/ssl_match_hostname/
ln -s %{python2_sitelib}/backports/ssl_match_hostname %{buildroot}/%{python2_sitelib}/urllib3/packages/ssl_match_hostname

%files -n python-%{pypi_name}
%doc README.rst dummyserver/certs/README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info

%changelog
* Fri May 01 2020 Cloud User - 1.24.2-1
- Initial package.
