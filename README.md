### Prepare

#### Disable selinux
```
sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
#### sudo reboot
```

#### Install epel-release
```
sudo yum install -y epel-release git libjpeg-turbo
```

#### Clone repo sentry-rpm
```
git clone https://github.com/patsevanton/sentry-rpm.git
cd sentry-rpm
```

#### Build and install general dependencies
```
./1general_dependencies.sh
```

#### Install and start PostgreSQL 9.6

```
./2postgresql.sh
```

#### Build and install python-dateutil rpm
```
./3dateutil.sh
```

#### Build and install python-urllib3 rpm
```
./4urllib3.sh
```

#### Build and install other dependencies rpm
```
./5other_dependencies.sh
```

#### Build and install sentry rpm
```
./6sentry.sh
```
