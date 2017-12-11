from exchanges.base import Exchange


class Gemini(Exchange):

    TICKER_URL = 'https://api.gemini.com/v1/pubticker/btcusd'

    @classmethod
    def _current_price_extractor(cls, data):
        return data.get('last')

    @classmethod
    def _current_bid_extractor(cls, data):
        return data.get('bid')

    @classmethod
    def _current_ask_extractor(cls, data):
        return data.get('ask')
