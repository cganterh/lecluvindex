.PHONY: install
install:
	pipenv $@ --dev

.PHONY: _test
_test: install
	flake8 .
