.PHONY: build upload

install:
	pip3 install --upgrade market-gpt

uninstall:
	pip3 uninstall market-gpt

build:
	python3 setup.py sdist

upload:
	twine upload dist/market-gpt-*.tar.gz
	rm dist/*.tar.gz

upload-test:
	twine upload --repository testpypi dist/*
	rm dist/market-gpt-*.tar.gz