#!/bin/bash

echo "Install nodejs and yarn"
curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
sudo yum install -y nodejs
sudo sed -e '/nodesource-source/,+6d' -i /etc/yum.repos.d/nodesource-el7.repo
curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo

cp spec/sentry-cron.service  spec/sentry-web.service  spec/sentry-worker.service ~/rpmbuild/SOURCES
spectool -g spec/sentry-9.1.2.spec
rpmbuild -bb sentry-9.1.2.spec
