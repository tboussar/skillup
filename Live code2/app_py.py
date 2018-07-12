from enum import Enum

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

class Machine:
    def __init__(self):
        self.amount = 0
        self.products = {
            "A": Product("Biscuits", 100),
            "B": Product("Coca", 120),
            "C": Product("Water", 85)
        }
        # self.coins = {}
        # for coin in Coin:
        #     self.coins[coin] = 10

        # self.coins = dict((coin, 10) for coin in Coin)
        self.coins = { coin: 10 for coin in Coin }

    def refill(self, code, quantity):
        self.products[code].quantity += quantity

    def insert(self, coin):
        self.amount += coin.value
        self.coins[coin] += 1

    def press(self, code):
        product = self.products[code]
        if self.amount >= product.price:
            if product.quantity > 0:
                product.quantity -= 1
                self.__change(self.amount - product.price)
                self.amount = 0
                return True
        return False

    def __change(self, change):
        if change == 0:
            return
        else:
            for coin in reversed(Coin):
                quantity = change // coin.value
                self.coins[coin] -= quantity
                change = change % coin.value
				