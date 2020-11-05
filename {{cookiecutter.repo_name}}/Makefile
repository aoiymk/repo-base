install:
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt --quiet
	@echo "Python dependencies installed successfully"
	@echo "Ready for work ✨"

requirements:
	pip freeze > requirements.txt	

delete-ds-store:
	find . -name ".DS_Store" -delete

lint:
	find . -iname "*.py" | xargs pylint

test:
	ptw -c .

test-ci:
	pytest -v .

optimus:
	make lint && make test-ci && requirements

create-environment:
	@pyenv virtualenv {{cookiecutter.python_version}}  {{cookiecutter.repo_name}} 
