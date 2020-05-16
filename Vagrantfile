ip = "192.168.33.198";

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.hostname = "sentry"
  config.vm.define "sentry"
  config.vm.network "private_network", ip: ip
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

end

