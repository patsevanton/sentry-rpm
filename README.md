### Prepare

echo "Disable selinux"

sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config

echo 'do not reboot'

echo "Install epel-release"

sudo yum install -y epel-release git

git clone https://github.com/patsevanton/sentry-rpm.git

cd sentry-rpm

Install dependencies

./build_dependencies_rpm.sh

Build and install python-dateutil rpm

./build_dateutil.sh

