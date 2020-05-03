#!/bin/bash

sudo -i -u sentry --config /etc/sentry/ upgrade
systemctl start sentry-worker
systemctl start sentry-cron
systemctl start sentry-web
