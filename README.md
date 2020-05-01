### Prepare

#### Disable selinux
```
sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
#### reboot if need
```

#### Install epel-release
```
sudo yum install -y epel-release git
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

#### Build and install python-dateutil rpm
```
./2dateutil.sh
```

#### Build and install python-urllib3 rpm
```
./3urllib3.sh
```

#### Build and install other dependencies rpm
```
./4other_dependencies.sh
```

#### Build and install sentry rpm
```
./sentry.sh
```
