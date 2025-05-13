import pytest


@pytest.fixture
def fake():
    from faker import Faker

    from faker_crypto import CryptoAddress

    Faker.seed(0)
    fake = Faker("en_US")
    fake.add_provider(CryptoAddress)

    return fake


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


def test_random_ripple_address(fake):
    for _ in range(100):
        address = fake.ripple_address()
        assert 25 <= len(address) <= 35


def test_ripple_address_startwith(fake):
    address = fake.ripple_address()
    assert address[0] == "r"


def test_ripple_address_chars(fake):
    # Ensure no excluded characters (0, O, I, l) are present
    excluded_chars = ["0", "O", "I", "l"]
    for _ in range(100):
        address = fake.ripple_address()
        for char in excluded_chars:
            assert char not in address[1:]  # Check suffix only


def test_random_tron_address(fake):
    for _ in range(100):
        address = fake.tron_address()
        assert len(address) == 34


def test_tron_address_startwith(fake):
    address = fake.tron_address()
    assert address[0] == "T"


def test_tron_address_chars(fake):
    # Ensure only Base58 characters are present in the suffix
    base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for _ in range(100):
        address = fake.tron_address()
        for char_in_addr in address[1:]:
            assert char_in_addr in base58_chars
