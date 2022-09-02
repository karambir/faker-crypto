import pytest
from faker_crypto import __version__


@pytest.fixture
def fake():
    from faker import Faker
    from faker_crypto import CryptoAddress

    Faker.seed(0)
    fake = Faker("en_US")
    fake.add_provider(CryptoAddress)

    return fake


def test_version():
    assert __version__ == "0.1.1"


def test_random_bitcoin_address(fake):
    for _ in range(100):
        address = fake.bitcoin_address()
        assert 25 <= len(address) <= 34


def test_bench32_bitcoin_address(fake):
    for _ in range(100):
        address = fake.bitcoin_address(include_bench32=True)
        assert 25 <= len(address) <= 36


def test_bitcoin_address_startwith(fake):
    address = fake.bitcoin_address()
    assert address[0] in ["1", "3"]


def test_bench32_bitcoin_address_startwith(fake):
    address = fake.bitcoin_address(include_bench32=True)
    assert address[:3] == "bc1" or address[0] in ["1", "3"]


def test_random_litecoin_address(fake):
    for _ in range(100):
        address = fake.litecoin_address()
        assert 26 <= len(address) <= 33


def test_litecoin_address_startwith(fake):
    address = fake.litecoin_address()
    assert address[0] in ["L", "M", "3"]


def test_random_ethereum_address(fake):
    for _ in range(100):
        address = fake.ethereum_address()
        assert len(address) == 40


def test_ethereum_address_startwith(fake):
    address = fake.ethereum_address()
    assert address[:2] == "0x"
