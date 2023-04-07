install:
	pip3 install -r requirements.txt

publish:
	python3 app.py publish

run:
	python3 app.py

.PHONY: install run publish
