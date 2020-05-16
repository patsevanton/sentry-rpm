#!/bin/bash

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
