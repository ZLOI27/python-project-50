install:
	uv sync

run:
	uv run gendiff

package-install:
	uv tool install --force dist/*.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff

lint:
	uv run ruff check

check: test lint

build:
	uv build

file-test:
	uv run gendiff /home/zk/python-project-50/file1.json /home/zk/python-project-50/file2.json

.PHONY: install test lint selfcheck check build

