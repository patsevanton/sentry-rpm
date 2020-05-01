#!/bin/bash

echo "Disable selinux"

sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
sudo reboot
