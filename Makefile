init:
	pip install -r requirements.txt
test:
	nose2 -v
venv:
	source ../venv/bin/activate
start:
	python main.py