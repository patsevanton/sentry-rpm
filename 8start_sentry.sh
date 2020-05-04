#!/bin/bash

sudo systemctl start redis
sudo -i -u sentry /usr/bin/sentry --config /etc/sentry/ upgrade
sudo systemctl start sentry-worker
sudo systemctl start sentry-cron
sudo systemctl start sentry-web
