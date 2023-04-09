install:
	pip3 install -r requirements.txt

publish:
	python3 app.py publish

image:
	python3 app.py image

run:
	python3 app.py

.PHONY: install run publish image
