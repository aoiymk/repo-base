install:
	@echo "Installing Python dependencies..."
	@pip3 install -r requirements.txt --quiet
	@echo "Python dependencies installed successfully"

delete-ds-store:
	find . -name ".DS_Store" -delete

lint:
	find . -iname "*.py" | xargs pylint

test:
	ptw -c .

test-ci:
	pytest -v .

optimus:
	make lint && make test-ci