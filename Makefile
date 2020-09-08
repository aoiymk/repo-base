make requirements:
	pip freeze > requirements.txt

install:
	@echo "Installing Python dependencies..."
	@pip3 install -r requirements.txt --quiet
	@echo "Python dependencies installed successfully"
	
delete-notebooks:
	find .  -name 'Untitled*' -delete  

delete-ds-store:
	find . -name ".DS_Store" -delete

lint:
	find . -iname "*.py" | xargs pylint

test:
	ptw -c .

test-ci:
	pytest -v .