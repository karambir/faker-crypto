# faker_crypto

__Version:__ 0.1.1

faker_crypto is a Faker provider for crytoaddreses.

Following crypto addresses are supported:

- Bitcoin
- Litecoin
- Ethereum

## Installation

Install with pip:

```bash
pip install faker-cypto
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
```


## Testing

Run unit tests with code coverage with:

```
pytest --cov -v 
```
