from string import hexdigits

from faker.providers import BaseProvider


class CryptoAddress(BaseProvider):
    coin_letters_integers = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    bech32_chars = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"

    def _ethereum_like_address(self) -> str:
        addr_length = 40
        address = ["0", "x"]

        address += self.random_elements(elements=list(hexdigits), length=addr_length)
        return "".join(address).lower()

    def bitcoin_address(self, include_bench32: bool = False) -> str:
        # Bitcoin addresses start with '1' or '3' and are 25-34 characters long.
        suffix_length = self.random_int(min=25, max=34)
        addr_prefix_space = ["1", "3"]
        if include_bench32:
            addr_prefix_space += ["bc1"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def bitcoincash_address(self) -> str:
        # Bitcoin Cash addresses start with 'q' or 'bitcoincash:q' and are 25-34 characters long.
        suffix_length = self.random_int(min=25, max=34)
        addr_prefix_space = ["q", "bitcoincash:q"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def litecoin_address(self) -> str:
        # Litecoin addresses start with 'L', 'M', or '3' and are 26-33 characters long.
        suffix_length = self.random_int(min=26, max=33)
        addr_prefix_space = ["L", "M", "3"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def dogecoin_address(self) -> str:
        # Dogecoin addresses start with '9', 'A', or 'D' and are 33 characters long.
        suffix_length = 33
        addr_prefix_space = ["9", "A", "D"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def ethereum_address(self) -> str:
        return self._ethereum_like_address()

    def polygon_address(self) -> str:
        return self._ethereum_like_address()

    def binance_smart_chain_address(self) -> str:
        return self._ethereum_like_address()

    def ripple_address(self) -> str:
        # Ripple addresses start with 'r' and are 25-35 characters long.
        # They use alphanumeric characters excluding "0", "O", "I", "l".
        ripple_chars = "rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"
        suffix_length = self.random_int(min=24, max=34)
        addr_prefix = "r"
        addr_suffix = "".join(self.random_elements(list(ripple_chars), suffix_length))
        return addr_prefix + addr_suffix

    def tron_address(self) -> str:
        # Tron addresses start with 'T' and are typically 34 characters long.
        suffix_length = 33
        addr_prefix = "T"
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))
        return addr_prefix + addr_suffix

    def polkadot_address(self) -> str:
        # Polkadot addresses (SS58 format for Polkadot network)
        # typically start with '1' and are around 47-48 characters long.
        suffix_length = self.random_int(min=46, max=47)
        addr_prefix = "1"
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))
        return addr_prefix + addr_suffix

    def cronos_address(self) -> str:
        return self._ethereum_like_address()

    def stellar_address(self) -> str:
        # Stellar addresses (public keys) start with 'G',
        # are 56 characters long, and use uppercase Base32 characters.
        stellar_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
        suffix_length = 55
        addr_prefix = "G"
        addr_suffix = "".join(self.random_elements(list(stellar_chars), suffix_length))
        return addr_prefix + addr_suffix

    def solana_address(self) -> str:
        # Solana addresses are Base58 encoded, 32-44 characters long.
        address_length = self.random_int(min=32, max=44)
        address = "".join(self.random_elements(list(self.coin_letters_integers), address_length))
        return address

    def zilliqa_address(self) -> str:
        # Zilliqa addresses use Bech32 encoding with HRP 'zil'.
        data_part_length = 38
        addr_prefix = "zil1"
        data_part = "".join(self.random_elements(list(self.bech32_chars), data_part_length))
        return addr_prefix + data_part

    def cardano_address(self) -> str:
        # Cardano Shelley-era addresses typically start with 'addr1'
        # and are Bech32 encoded.
        data_part_length = self.random_int(min=55, max=59)  # gives total length 60-64
        addr_prefix = "addr1"
        data_part = "".join(self.random_elements(list(self.bech32_chars), data_part_length))
        return addr_prefix + data_part

    def hedera_address(self) -> str:
        # Hedera account IDs are in the format shardNum.realmNum.accountNum
        # Shard and Realm are typically 0.
        # Account number is a non-negative integer.
        shard_num = 0
        realm_num = 0
        account_num = self.random_int(min=1000, max=9999999)
        return f"{shard_num}.{realm_num}.{account_num}"

    def optimism_address(self) -> str:
        return self._ethereum_like_address()

    def arbitrum_address(self) -> str:
        return self._ethereum_like_address()

    def avalanche_cchain_address(self) -> str:
        return self._ethereum_like_address()
