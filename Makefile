.DEFAULT_GOAL := help
.PHONY: deps tox test test-all-versions help

REPO_ROOT:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

deps: ## install deps (library & development)
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

tox: ## run ALL checks for ALL available python versions
	python -m tox

test: ## run tests ONLY for current python version
	python -m pytest

test-all-versions: ## run test for multiple python versions using docker
	# python 3.10 not provided in image so we skip it
	docker run --rm -v $(REPO_ROOT):/src fkrull/multi-python tox -c /src -e py36,py37,py38,py39

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
