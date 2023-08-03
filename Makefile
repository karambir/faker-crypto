.DEFAULT_GOAL := help
SHELL := bash
.ONESHELL:


.PHONY: help
help:            ## show the help
	@echo "Usage: make <target>"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Run `poetry install`
	poetry install

showdeps: ## run poetry to show deps
	@echo "CURRENT:"
	poetry show --tree
	@echo
	@echo "LATEST:"
	poetry show --latest

lint: ## Runs black, isort, bandit, flake8 in check mode
	poetry run black --check .
	poetry run isort --check-only .
	poetry run flake8 faker_crypto tests

format: ## Formats you code with Black
	poetry run isort .
	poetry run black .

test: ## run pytest with coverage
	poetry run pytest --cov -v .

build: install lint test ## run `poetry build` to build source distribution and wheel
	poetry build

release-patch: build ## Make patch release
	poetry run bump2version --verbose patch

release-minor: build ## Make minor release
	poetry run bump2version --verbose minor
