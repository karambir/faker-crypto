# faker-crypto

__Version:__ 0.2.1

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
fake.binance_smart_chain_address()
# '0xceeea432e1eb0fdcbd7ffbe2e7fefa6ccb78dd'
fake.polygon_address()
# '0x32f065b1fe349fcaa29bfdfa5e6aae25a53203'
```


## Testing

Run unit tests with code coverage with:

```
pytest --cov -v 
```
