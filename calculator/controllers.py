from calculator.models import ExchangeRate


class ExchangeRateController(object):

    def calculate_amount(self, from_currency, to_currency, amount):
        pair = ExchangeRate.objects.get(currency_pair=f"{from_currency}/{to_currency}")
        return amount * pair.exchange_rate

    def get_all_pairs(self):
        return ExchangeRate.objects.all()
