from string import hexdigits

from faker.providers import BaseProvider


class CryptoAddress(BaseProvider):
    coin_letters_integers = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

    def _ethereum_like_address(self) -> str:
        addr_length = 40
        address = ["0", "x"]

        address += self.random_elements(elements=list(hexdigits), length=addr_length - 2)
        return "".join(address).lower()

    def bitcoin_address(self, include_bench32: bool = False) -> str:
        suffix_length = self.random_int(min=25, max=34)
        addr_prefix_space = ["1", "3"]
        if include_bench32:
            addr_prefix_space += ["bc1"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def bitcoincash_address(self) -> str:
        suffix_length = self.random_int(min=25, max=34)
        addr_prefix_space = ["q", "bitcoincash:q"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def litecoin_address(self) -> str:
        suffix_length = self.random_int(min=26, max=33)
        addr_prefix_space = ["L", "M", "3"]

        addr_prefix = self.random_element(elements=addr_prefix_space)
        addr_suffix = "".join(self.random_elements(list(self.coin_letters_integers), suffix_length))

        return addr_prefix + addr_suffix

    def dogecoin_address(self) -> str:
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
