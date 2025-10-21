ping:
	ansible all -m ping -i inventory.ini

bootstrap:
	ansible-playbook -i inventory.ini playbooks/bootstrap.yml

docker:
	ansible-playbook -i inventory.ini playbooks/docker.yml

portainer:
	ansible-playbook -i inventory.ini playbooks/portainer.yml

home-assistant:
	ansible-playbook -i inventory.ini playbooks/home-assistant.yml

ssh:
	ssh admin@192.168.0.105
