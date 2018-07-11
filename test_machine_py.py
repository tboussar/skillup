import unittest
from app import Machine, Coin

class TestMachine(unittest.TestCase):
    def test_init_products_quantity_is_zero(self):
        machine = Machine()
        self.assertEquals(machine.products["A"].quantity, 0)

    def test_init_coins(self):
        machine = Machine()
        self.assertEquals(machine.coins[Coin.NICKEL], 10)
        self.assertEquals(machine.coins[Coin.DIME], 10)
        self.assertEquals(machine.coins[Coin.QUARTER], 10)
        self.assertEquals(machine.coins[Coin.DOLLAR], 10)

    def test_refill_product(self):
        machine = Machine()
        machine.refill("A", 5)
        self.assertEquals(machine.products["A"].quantity, 5)

    def test_insert_coin(self):
        machine = Machine()
        machine.insert(Coin.QUARTER)
        self.assertEquals(machine.amount, Coin.QUARTER.value)
        self.assertEquals(machine.coins[Coin.QUARTER], 11)

    def test_buy_product(self):
        machine = Machine()
        machine.refill("A", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("A")
        self.assertTrue(outcome)
        self.assertEquals(machine.products["A"].quantity, 0)
        self.assertEquals(machine.amount, 0)
        self.assertEquals(machine.coins[Coin.DOLLAR], 11)

    def test_try_buy_product_not_enough_money(self):
        machine = Machine()
        machine.refill("A", 1)
        machine.insert(Coin.QUARTER)
        machine.insert(Coin.QUARTER)
        outcome = machine.press("A")
        self.assertEquals(outcome, False)
        self.assertEquals(machine.products["A"].quantity, 1)
        self.assertEquals(machine.amount, 50)

    def test_try_buy_product_not_enough_stock(self):
        machine = Machine()
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("A")
        self.assertEquals(outcome, False)
        self.assertEquals(machine.products["A"].quantity, 0)
        self.assertEquals(machine.amount, 100)

    def test_give_too_much_money_with_stock(self):
        machine = Machine()
        machine.refill("C", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("C")
        self.assertEquals(outcome, True)
        self.assertEquals(machine.coins[Coin.DOLLAR], 11)
        self.assertEquals(machine.coins[Coin.DIME], 9)
        self.assertEquals(machine.coins[Coin.NICKEL], 9)
        self.assertEquals(machine.amount, 0)
