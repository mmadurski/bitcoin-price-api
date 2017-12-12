from decimal import Decimal

from exchanges.base import Exchange
from exchanges.helpers import get_response


class Coinbase(Exchange):

    TICKER_URL = 'https://api.coinbase.com/v2/prices/BTC-{}/{}'

    @classmethod
    def get_current_price(cls, currency='USD'):
        url = cls.TICKER_URL.format(currency, 'spot')
        data = get_response(url)
        price = data.get('data').get('amount')
        return Decimal(price)

    @classmethod
    def get_current_bid(cls):
        return None

    @classmethod
    def get_current_ask(cls):
        return None
