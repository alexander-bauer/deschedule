.PHONY: requirements upgrade bower db archpkg

requirements: requirements.txt
	python3 -m venv flask
	flask/bin/pip install --requirement requirements.txt

upgrade: requirements
	flask/bin/pip install --upgrade --requirement requirements.txt

bower:
	bower install mui

db: app/models.py
	./db_create.py

app.db: db

archpkg: contrib/PKGBUILD
	cd contrib/; makepkg --holdver --clean --cleanbuild --force
