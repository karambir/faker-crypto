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
        assert len(address) == 42


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


def test_random_polkadot_address(fake):
    for _ in range(100):
        address = fake.polkadot_address()
        assert 47 <= len(address) <= 48


def test_polkadot_address_startwith(fake):
    address = fake.polkadot_address()
    assert address[0] == "1"


def test_polkadot_address_chars(fake):
    # Ensure only Base58 characters (excluding 0, O, I, l) are present in the suffix
    base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for _ in range(100):
        address = fake.polkadot_address()
        for char_in_addr in address[1:]:
            assert char_in_addr in base58_chars


def test_random_cronos_address(fake):
    for _ in range(100):
        address = fake.cronos_address()
        assert len(address) == 42


def test_cronos_address_startwith(fake):
    address = fake.cronos_address()
    assert address[:2] == "0x"


def test_cronos_address_chars(fake):
    # Ensure only hex characters are present in the suffix
    hex_chars = "0123456789abcdefABCDEF"
    for _ in range(100):
        address = fake.cronos_address()
        for char_in_addr in address[2:]:
            assert char_in_addr in hex_chars


def test_random_stellar_address(fake):
    for _ in range(100):
        address = fake.stellar_address()
        assert len(address) == 56


def test_stellar_address_startwith(fake):
    address = fake.stellar_address()
    assert address[0] == "G"


def test_stellar_address_chars(fake):
    # Ensure only uppercase Base32 characters are present in the suffix
    stellar_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    for _ in range(100):
        address = fake.stellar_address()
        for char_in_addr in address[1:]:
            assert char_in_addr in stellar_chars


def test_random_solana_address(fake):
    for _ in range(100):
        address = fake.solana_address()
        assert 32 <= len(address) <= 44


def test_solana_address_chars(fake):
    # Ensure only Base58 characters are present
    base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for _ in range(100):
        address = fake.solana_address()
        for char_in_addr in address:
            assert char_in_addr in base58_chars


def test_random_zilliqa_address(fake):
    for _ in range(100):
        address = fake.zilliqa_address()
        assert len(address) == 42


def test_zilliqa_address_startwith(fake):
    address = fake.zilliqa_address()
    assert address.startswith("zil1")


def test_zilliqa_address_chars(fake):
    # Ensure only Bech32 characters are present in the data part
    bech32_chars = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
    for _ in range(100):
        address = fake.zilliqa_address()
        for char_in_addr in address[4:]:
            assert char_in_addr in bech32_chars


def test_random_cardano_address(fake):
    for _ in range(100):
        address = fake.cardano_address()
        assert 60 <= len(address) <= 64  # 'addr1' + 55 to 59 chars


def test_cardano_address_startwith(fake):
    address = fake.cardano_address()
    assert address.startswith("addr1")


def test_cardano_address_chars(fake):
    # Ensure only Bech32 characters (lowercase) are present in the data part
    bech32_chars = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
    for _ in range(100):
        address = fake.cardano_address()
        for char_in_addr in address[5:]:
            assert char_in_addr in bech32_chars


def test_random_hedera_address(fake):
    for _ in range(100):
        address = fake.hedera_address()
        parts = address.split(".")
        assert len(parts) == 3
        assert parts[0] == "0"
        assert parts[1] == "0"
        assert 1000 <= int(parts[2]) <= 9999999
        assert address.startswith("0.0.")


def test_random_optimism_address(fake):
    for _ in range(100):
        address = fake.optimism_address()
        assert len(address) == 42


def test_optimism_address_startwith(fake):
    address = fake.optimism_address()
    assert address.startswith("0x")


def test_optimism_address_chars(fake):
    # Ensure only hex characters are present in the suffix
    hex_chars = "0123456789abcdefABCDEF"
    for _ in range(100):
        address = fake.optimism_address()
        for char_in_addr in address[2:]:
            assert char_in_addr in hex_chars


def test_random_arbitrum_address(fake):
    for _ in range(100):
        address = fake.arbitrum_address()
        assert len(address) == 42


def test_arbitrum_address_startwith(fake):
    address = fake.arbitrum_address()
    assert address.startswith("0x")


def test_arbitrum_address_chars(fake):
    # Ensure only hex characters are present in the suffix
    hex_chars = "0123456789abcdefABCDEF"
    for _ in range(100):
        address = fake.arbitrum_address()
        for char_in_addr in address[2:]:
            assert char_in_addr in hex_chars


def test_random_avalanche_cchain_address(fake):
    for _ in range(100):
        address = fake.avalanche_cchain_address()
        assert len(address) == 42


def test_avalanche_cchain_address_startwith(fake):
    address = fake.avalanche_cchain_address()
    assert address.startswith("0x")


def test_avalanche_cchain_address_chars(fake):
    # Ensure only hex characters are present in the suffix
    hex_chars = "0123456789abcdefABCDEF"
    for _ in range(100):
        address = fake.avalanche_cchain_address()
        for char_in_addr in address[2:]:
            assert char_in_addr in hex_chars


def test_random_polygon_address(fake):
    for _ in range(100):
        address = fake.polygon_address()
        assert len(address) == 42


def test_polygon_address_startwith(fake):
    address = fake.polygon_address()
    assert address[:2] == "0x"


def test_random_binance_smart_chain_address(fake):
    for _ in range(100):
        address = fake.binance_smart_chain_address()
        assert len(address) == 42


def test_binance_smart_chain_address_startwith(fake):
    address = fake.binance_smart_chain_address()
    assert address[:2] == "0x"
