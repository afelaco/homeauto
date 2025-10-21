.PHONY: bootstrap
bootstrap:
	bash ./bootstrap/main.sh

pre-commit-autoupdate:
	uv run pre-commit autoupdate

pre-commit-run:
	uv run pre-commit run --all-files

list-ssh:
	ls -l ~/.ssh/id_*

view-public-ssh:
	@echo "Public key contents:"
	cat ~/.ssh/id_rsa.pub

view-private-ssh:
	@echo "Public key contents:"
	cat ~/.ssh/id_rsa

fingerprint:
	@echo "Fingerprint of $(KEY).pub:"
	ssh-keygen -lf $(KEY).pub

passphrase:
	@ssh-keygen -p -f $(KEY)

knownhosts:
	@ssh-keygen -R $(HOST)
