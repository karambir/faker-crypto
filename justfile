# Faker Crypto development tasks
# Install 'just' from https://github.com/casey/just

# List all available recipes
default:
    @just --list

# Install development dependencies using uv
install:
    uv sync --frozen --group dev

# Install only the package without dev dependencies
install-prod:
    uv sync --frozen --no-dev

# Create/update uv.lock file from pyproject.toml
lock:
    uv lock

# Run tests
test:
    uv run pytest

# Run tests with coverage
test-cov:
    uv run pytest --cov=faker_crypto --cov-report=term-missing

# Update dependencies using uv and regenerate lock file
update:
    uv lock --upgrade

# Run code quality tools
lint:
    uv run ruff format --check src tests
    uv run ruff check src tests

# Format code with ruff
format:
    uv run ruff format src tests
    uv run ruff check --fix src tests

# Build the package
build:
    uv build

# Clean build artifacts
clean:
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info/
    find . -type d -name __pycache__ -exec rm -rf {} +

# Run all quality checks
check: lint test

# Set up pre-commit hooks
precommit-setup:
    uv run pre-commit install

# Update pre-commit hooks
precommit-update:
    uv run pre-commit autoupdate

# Run all pre-commit hooks on all files
precommit-run:
    uv run pre-commit run --all-files
