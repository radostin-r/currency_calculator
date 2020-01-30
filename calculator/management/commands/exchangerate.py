import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from django.db import IntegrityError

from calculator.models import ExchangeRate


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'http://bnb.bg/Statistics/StExternalSector/StExchangeRates/StERForeignCurrencies/index.htm'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        tbody = soup.find_all('tr')
        for row in tbody:
            currency = row.select_one('td:nth-of-type(2)')
            if currency:
                currency = row.select_one('td:nth-of-type(2)').get_text()
                currency_to_bgn_rate = row.select_one('td:nth-of-type(4)')

                # check whether td exists
                if currency_to_bgn_rate:
                    currency_to_bgn_rate = currency_to_bgn_rate.get_text()

                bgn_to_currency_rate = row.select_one('td:nth-of-type(5)')
                if bgn_to_currency_rate:
                    bgn_to_currency_rate = bgn_to_currency_rate.get_text()

                # check whether td has a value
                if currency_to_bgn_rate:
                    self.save_pair(f"{currency}/BGN", float(currency_to_bgn_rate))

                if bgn_to_currency_rate:
                    self.save_pair(f"BGN/{currency}", float(bgn_to_currency_rate))

        self.stdout.write(self.style.SUCCESS('Successfully pull BNB exchange rates'))

    def save_pair(self, currency_pair, exchange_rate):
        # catch integrity error because get_or_create or update_or_create don't do the job
        # due to db constrainsts
        try:
            pair = ExchangeRate.objects.get_or_create(currency_pair=currency_pair)
            pair = pair[0]
        except IntegrityError:
            pair = ExchangeRate()
            pair.currency_pair = currency_pair
        pair.exchange_rate = exchange_rate
        pair.save()
