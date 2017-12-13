from exchanges.base import Exchange


class Cex(Exchange):

    TICKER_URL = 'https://cex.io/api/ticker/BTC/USD'

    @classmethod
    def _current_price_extractor(cls, data):
        return data.get('last')

    @classmethod
    def _current_bid_extractor(cls, data):
        return data.get('bid')

    @classmethod
    def _current_ask_extractor(cls, data):
        return data.get('ask')
