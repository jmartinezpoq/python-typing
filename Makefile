py_files = $(wildcard *.py) 

env_ok: requirements.txt
	rm -rf env env_ok
	python3 -m venv env
	env/bin/pip install -r requirements.txt
	touch env_ok

check: env_ok
	env/bin/mypy $(py_files)