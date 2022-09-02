__version__ = "0.1.1"


from string import hexdigits

from faker.providers import BaseProvider


class CryptoAddress(BaseProvider):
    coin_letters_integers = "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

    def bitcoin_address(self) -> str:
        address_length = self.random_int(min=25, max=34)
        address = ["1", "3"]

        address += self.random_elements(elements=list(self.coin_letters_integers), length=address_length - 2)
        return "".join(address)

    def litecoin_address(self) -> str:
        address_length = self.random_int(min=26, max=33)
        address = ["L", "M", "3"]

        address += self.random_elements(elements=list(self.coin_letters_integers), length=address_length - 3)
        return "".join(address)

    def ethereum_address(self) -> str:
        address_length = 40
        address = ["0", "x"]

        address += self.random_elements(elements=list(hexdigits), length=address_length - 2)
        return "".join(address).lower()
