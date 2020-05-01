#!/bin/bash

echo "Build urllib rpm"
spectool -g -R spec/urllib3-1.24.2.spec
rpmbuild --bb spec/urllib3-1.24.2.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python-dateutil-2.4.2-1.el7.noarch.rpm
