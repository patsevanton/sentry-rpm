#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

mkdir -p ./{RPMS,SRPMS,BUILD,SOURCES,SPECS}
cp sentry-cron.service  sentry-web.service  sentry-worker.service SOURCES
spectool -g -C SOURCES sentry-9.1.2.spec
rpmbuild --quiet --define "_topdir `pwd`" -bb sentry-9.1.2.spec
