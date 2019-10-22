setup:
	python3 -m venv /home/alari/dev/start_aws/aws_base_setup/project

install:
	pip install -r requirements.txt
	pip install -U pytest

test:
	#PYTHONPATH=. && pytest -vv --cov=~/dev/start_aws/aws_base_setup ~/dev/start_aws/aws_base_setup/tests/*.py
	
	python -m pytest ~/dev/start_aws/aws_base_setup/tests/*.py
lint:
	pylint --disable=R, C aws_base_setup/s3.py

all : install test lint

