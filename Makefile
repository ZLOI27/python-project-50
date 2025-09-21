install:
	uv sync

run:
	uv run gendiff

package-install:
	uv tool install --force dist/*.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml tests/

test-coverage-without-xml:
	uv run pytest --cov=gendiff

lint:
	uv run ruff check

check: test lint

build:
	uv build

file-test:
	uv run gendiff /home/zk/python-project-50/tests/test_data/file1.json /home/zk/python-project-50/tests/test_data/file2.json

full-check: test-coverage-without-xml file-test lint 

.PHONY: install test lint selfcheck check build

