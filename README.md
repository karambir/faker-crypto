# faker-crypto

[![CI](https://github.com/karambir/faker-crypto/actions/workflows/ci.yml/badge.svg)](https://github.com/karambir/faker-crypto/actions/workflows/ci.yml)
[![PyPI Version](https://img.shields.io/pypi/v/faker-crypto.svg)](https://pypi.org/project/faker-crypto/)
[![Python Versions](https://img.shields.io/pypi/pyversions/faker-crypto.svg)](https://pypi.org/project/faker-crypto/)

faker-crypto is a Faker provider for Cryto Addreses.

Following crypto addresses are supported:

- Bitcoin
- Bitcoin Cash
- Litecoin
- Dogecoin
- Ethereum
- Binance Smart Chain
- Polygon

## Installation

Install with pip:

```bash
pip install faker-crypto
```

## Usage

Add `CryptoAddress` provider to Faker instance:

```python
from faker import Faker
from faker_crypto import CryptoAddress

fake = Faker()
fake.add_provider(CryptoAddress)

fake.bitcoin_address()
# '13XTsE8TKEHW5zAmCWmBvNk5KvEcEjVQu'
fake.litecoin_address()
# 'LM3HgLcPemiBb5MJ3vqRRPrPqBdtf7pL'
fake.ethereum_address()
# '0x7ea8abae70ce7e9ce09155ee9169d5f18fc96b'
fake.binance_smart_chain_address()
# '0xceeea432e1eb0fdcbd7ffbe2e7fefa6ccb78dd'
fake.polygon_address()
# '0x32f065b1fe349fcaa29bfdfa5e6aae25a53203'
```

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

### Setup Development Environment

```bash
# Install project in development mode with all dependencies
uv sync --frozen --dev

# Or use just command
just install
```

### Testing

Run unit tests with code coverage with:

```bash
uv run pytest --cov -v

# Or use just command
just test
```

### Formatting and Linting

```bash
# Format code
just format

# Run linters
just lint
```
