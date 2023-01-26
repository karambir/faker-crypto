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
    assert __version__ == "0.2.0"


def test_random_bitcoin_address(fake):
    for _ in range(100):
        address = fake.bitcoin_address()
        assert 26 <= len(address) <= 35


def test_bench32_bitcoin_address(fake):
    for _ in range(100):
        address = fake.bitcoin_address(include_bench32=True)
        assert 26 <= len(address) <= 37


def test_bitcoin_address_startwith(fake):
    address = fake.bitcoin_address()
    assert address[0] in ["1", "3"]


def test_bench32_bitcoin_address_startwith(fake):
    for _ in range(100):
        address = fake.bitcoin_address(include_bench32=True)
        assert address[:3] == "bc1" or address[0] in ["1", "3"]


def test_random_bitcoincash_address(fake):
    for _ in range(100):
        address = fake.bitcoincash_address()
        assert 26 <= len(address) <= 47


def test_bitcoincash_address_startwith(fake):
    for _ in range(100):
        address = fake.bitcoincash_address()
        assert address[0] == "q" or "bitcoincash:q" in address


def test_random_litecoin_address(fake):
    for _ in range(100):
        address = fake.litecoin_address()
        assert 27 <= len(address) <= 34


def test_litecoin_address_startwith(fake):
    address = fake.litecoin_address()
    assert address[0] in ["L", "M", "3"]


def test_random_dogecoin_address(fake):
    for _ in range(100):
        address = fake.dogecoin_address()
        assert len(address) == 34


def test_dogecoin_address_startwith(fake):
    address = fake.dogecoin_address()
    assert address[0] in ["9", "A", "D"]


def test_random_ethereum_address(fake):
    for _ in range(100):
        address = fake.ethereum_address()
        assert len(address) == 40


def test_ethereum_address_startwith(fake):
    address = fake.ethereum_address()
    assert address[:2] == "0x"
