#!/bin/bash

echo "Disable selinux"

sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config

read -r -p "Are you sure? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
    sudo reboot
else
    echo 'do not reboot'
fi

