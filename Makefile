.PHONY: init
init:
	pip install -r requirements.txt


.PHONY: test
test:
	pytest tests
