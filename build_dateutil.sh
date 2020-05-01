#!/bin/bash

echo "Build and install python-dateutil rpm"
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS,SPECS}
spectool -g -R spec/python-dateutil.spec
wget https://raw.githubusercontent.com/patsevanton/sentry-rpm/master/spec/python-dateutil-system-zoneinfo.patch -P ~/rpmbuild/SOURCES
wget https://raw.githubusercontent.com/patsevanton/sentry-rpm/master/spec/python-dateutil-timelex-string.patch -P ~/rpmbuild/SOURCES
rpmbuild --bb spec/python-dateutil.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python-dateutil-2.4.2-1.el7.noarch.rpm
