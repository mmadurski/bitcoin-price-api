from decimal import Decimal

from exchanges.base import Exchange
from exchanges.helpers import get_response


class Coinbase(Exchange):

    TICKER_URL = 'https://api.coinbase.com/v2/prices/BTC-{}/{}'

    @classmethod
    def _get_current_price(cls, currency='USD', price_type='spot'):
        url = cls.TICKER_URL.format(currency, price_type)
        data = get_response(url)
        price = data.get('data').get('amount')
        return Decimal(price)

    @classmethod
    def get_current_price(cls, currency='USD'):
        return cls._get_current_price(currency=currency, price_type='spot')

    @classmethod
    def get_current_bid(cls, currency='USD'):
        return cls._get_current_price(currency=currency, price_type='buy')

    @classmethod
    def get_current_ask(cls, currency='USD'):
        return cls._get_current_price(currency=currency, price_type='sell')
