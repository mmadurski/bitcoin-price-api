import unittest
from decimal import Decimal


from exchanges.coindesk import CoinDesk


class CoinDeskDecimalConverstion(unittest.TestCase):
    def setUp(self):
        self.x = CoinDesk()

    def test_current_price(self):
        price = self.x.get_current_price()
        self.assertEqual(
            type(price),
            Decimal
        )

    def test_past_price(self):
        price = self.x.get_past_price('2017-01-01')
        self.assertEqual(
            type(price),
            Decimal
        )

    def test_historical_data_as_dict(self):
        prices = self.x.get_historical_data_as_dict(start='2017-01-01', end='2017-01-03')
        for price in prices.values():
            self.assertEqual(
                type(price),
                Decimal
            )

    def test_historical_data_as_list(self):
        prices = self.x.get_historical_data_as_list(start='2017-01-01', end='2017-01-03')
        for price in prices:
            self.assertEqual(
                type(price['price']),
                Decimal
            )


if __name__ == '__main__':
    unittest.main()
