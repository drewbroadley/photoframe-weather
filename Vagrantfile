# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.7.0"

# Set working project folder
PROJECT_FOLDER = 'photoframe_weather'

Vagrant.configure(2) do |config|

  # Vagrant 1.8.4 has a bug not alowing latest LTS to sync drives - 19/06/2016
  # config.vm.box = "ubuntu/xenial64"
  config.vm.box = "ubuntu/trusty64"

  # Forward agent
  config.ssh.forward_agent = true

  # Sync base folder Xenial64
  # config.vm.synced_folder ".", "/home/ubuntu/" + PROJECT_FOLDER
  config.vm.synced_folder ".", "/home/vagrant/" + PROJECT_FOLDER

  config.vm.network "forwarded_port", guest: 5432, host: 5542
  config.vm.network "forwarded_port", guest: 8000, host: 8071

  config.vm.provision "ansible_local" do |ansible|
    ansible.verbose = "v"
    # Provision path for Xenial64
    # ansible.provisioning_path = "/home/ubuntu/"
    ansible.provisioning_path = "/home/vagrant/" + PROJECT_FOLDER + "/"
    ansible.playbook = "provision/vagrant.yml"
  end
  
  # Run local "Vagrantfile.local" file for custom configurations (not in VCS)
  if File.exist? "Vagrantfile.local"
    instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
  end
end

