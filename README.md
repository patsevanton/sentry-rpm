### Prepare

echo "Disable selinux"
sudo sed -i s/^SELINUX=.*$/SELINUX=disabled/ /etc/selinux/config
echo 'do not reboot'

echo "Install epel-release"
sudo yum install -y epel-release

echo "Install dependencies"
sudo yum install -y cargo gcc gcc-c++ git libffi-devel libjpeg-devel libxml2-devel \
libxslt libxslt-devel make mc openssl-devel postgresql-devel python-devel \
python-lxml python-nose python3-pip python34 rpm-build rpmdevtools \
ruby-devel rubygems zlib-devel
