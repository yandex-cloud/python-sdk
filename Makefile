.DEFAULT_GOAL := help
.PHONY: deps tox tox-current test lint format test-all-versions help

REPO_ROOT:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

deps: ## install deps (library & development)
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements-dev.txt

deps-genproto: ## install deps (library & development)
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements-genproto.txt

tox: ## run ALL checks for ALL available python versions
	python3 -m tox

tox-current: ## run ALL checks ONLY for current python version
	python3 -m tox -e `python3 -c 'import platform; print("py" + "".join(platform.python_version_tuple()[:2]))'`

test: ## run tests ONLY for current python version
	python3 -m pytest

lint: ## run linters, formatters for current python versions
	python3 -m flake8 yandexcloud
	python3 -m pylint yandexcloud

format:
	python3 -m isort yandexcloud setup.py changelog.py tests
	python3 -m black yandexcloud setup.py changelog.py tests

test-all-versions: ## run test for multiple python versions using docker
	# python 3.12 not provided in image so we skip it
	docker run --rm -v $(REPO_ROOT):/src ghcr.io/fkrull/docker-multi-python:bionic tox -c /src -e py38,py39,py310,py311

submodule:  ## update submodules
	git submodule update --init --recursive --remote

proto:  ## regenerate code from protobuf
	rm -rf yandex
	python3 -m grpc_tools.protoc \
        --proto_path=cloudapi \
        --proto_path=cloudapi/third_party/googleapis \
        --python_out=. \
        --grpc_python_out=. \
        `find cloudapi/yandex -name '*.proto'`
	find yandex -type d -exec touch {}/__init__.py \;

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
