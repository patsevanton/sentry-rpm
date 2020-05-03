#!/bin/bash

echo "Build sentry-ldap-auth rpm"
spectool -g -R spec/sentry-ldap-auth-2.8.1.spec
sudo yum-builddep -y spec/sentry-ldap-auth-2.8.1.spec
rpmbuild --bb spec/sentry-ldap-auth-2.8.1.spec
sudo yum install -y ~/rpmbuild/RPMS/x86_64/python2-sentry-ldap-auth-2.8.1
