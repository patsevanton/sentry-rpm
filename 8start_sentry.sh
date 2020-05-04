#!/bin/bash

sudo -i -u sentry --config /etc/sentry/ upgrade
sudo systemctl start sentry-worker
sudo systemctl start sentry-cron
sudo systemctl start sentry-web
