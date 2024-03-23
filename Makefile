install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

format:
	black *.py

# personal and not click-setup-installed commands
api:
	python $(CURDIR)/api.py