init:
	pip install -r requirements.txt

test:
	nosetests tests

lint:
	flake8 fold_to_ascii
	flake8 tests
