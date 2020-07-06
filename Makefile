venv/bin/python:
	virtualenv venv
	venv/bin/pip install -r requirements.txt

.PHONY: test
test: venv/bin/python
	venv/bin/flake8 --config=.flake8
	venv/bin/nosetests --verbosity=2

.PHONY: pipelines
pipelines:
	ls -1 pipelines | xargs -I {} sh -c "cd pipelines/{} && make"