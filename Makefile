install:
	pip3 install -r requirements.txt

publish:
	python3 app.py publish

template:
	python3 app.py template

run:
	python3 app.py

.PHONY: install run publish template
