ping:
	ansible all -m ping -i inventory.ini

bootstrap:
	ansible-playbook -i inventory.ini playbooks/bootstrap.yml

docker:
	ansible-playbook -i inventory.ini playbooks/docker.yml

portainer:
	ansible-playbook -i inventory.ini playbooks/portainer.yml
