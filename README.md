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
./build_general_dependencies.sh
```

#### Build and install python-dateutil rpm
```
./build_dateutil.sh
```

1general_dependencies.sh
2dateutil.sh
3urllib3.sh
4other_dependencies.sh
