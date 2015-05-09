# -*- mode: ruby -*-
# vi: set ft=ruby :

# Set a name in the VirtualBox GUI
NAME="scrumblr"

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "precise32"
  config.vm.box_url="http://files.vagrantup.com/precise32.box"

  config.vm.network :forwarded_port, guest: 8080, host: 8080, auto_correct: true

  config.vm.provider :virtualbox do |vb|
    vb.name = 'scrumblr'
    vb.memory = 512
    #vb.gui = true
  end
 
  config.vm.provision :shell, path: "provisioning/provision.sh"

end
