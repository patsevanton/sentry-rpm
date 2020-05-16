#!/bin/bash

echo "Build pyasn1 to rpm"
fpm -s python -t rpm pyasn1
sudo yum install -y python-pyasn1-0.4.8-1.noarch.rpm

echo "Build pyasn1-modules to rpm"
fpm -s python -t rpm pyasn1-modules
sudo yum install -y python-pyasn1-modules-0.2.8-1.noarch.rpm

echo "Build django-auth-ldap to rpm"
spectool -g -R spec/django-auth-ldap-1.2.17.spec
sudo yum-builddep -y spec/django-auth-ldap-1.2.17.spec
rpmbuild -bb spec/django-auth-ldap-1.2.17.spec
sudo yum install -y ~/rpmbuild/RPMS/noarch/python2-django-auth-ldap-1.2.17-1.el7.noarch.rpm

echo "Build sentry-ldap-auth to rpm"
spectool -g -R spec/sentry-ldap-auth-2.8.1.spec
sudo yum-builddep -y spec/sentry-ldap-auth-2.8.1.spec
rpmbuild -bb spec/sentry-ldap-auth-2.8.1.spec
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-sentry-ldap-auth-2.8.1

