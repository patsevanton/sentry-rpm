Name:           python-dateutil
Version:        2.4.2
Release:        1%{?dist}
Summary:        Powerful extensions to the standard datetime module

Group:          Development/Languages
License:        Python
URL:            https://github.com/dateutil/dateutil
Source0:        https://github.com/dateutil/dateutil/archive/%{version}.tar.gz
# https://github.com/dateutil/dateutil/issues/11
Patch0:         python-dateutil-system-zoneinfo.patch
Patch1:         python-dateutil-timelex-string.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
#BuildRequires:  python-sphinx
BuildRequires:  python-six
Requires:       tzdata
Requires:       python-six
Conflicts:      python-vobject <= 0.8.1c-10

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

%description
The dateutil module provides powerful extensions to the standard datetime
module available in Python 2.3+.

This is the version for Python 2.

%prep
%autosetup -p0 -n dateutil-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 NEWS > NEWS.new
mv NEWS.new NEWS

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

%check
%{__python2} setup.py test

%files
%license LICENSE
%doc NEWS README.rst
%{python2_sitelib}/dateutil/
%{python2_sitelib}/*.egg-info
