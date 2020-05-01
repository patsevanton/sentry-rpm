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

#### Install dependencies
```
./build_dependencies_rpm.sh
```

#### Build and install python-dateutil rpm
```
./build_dateutil.sh
```
