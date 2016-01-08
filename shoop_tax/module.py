from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from shoop.core import taxing
from shoop.core.models import Tax
from shoop.core.pricing import TaxfulPrice, TaxlessPrice
from shoop.core.taxing import TaxedPrice, LineTax

import requests


class AvaTaxModule(taxing.TaxModule):

    identifier = "avalara_tax"
    name = _("Avalara Taxation")

    def get_taxed_price_for(self, context, item, price):
        return _calculate_taxes(price, context)


def _calculate_taxes(price, taxing_context):
    """
    Caculate tax using PyAvaTax

    :param price:
    :param taxing_context:
    :param tax_class:
    :return:
    """
    base_price = TaxlessPrice(price)
    postal_code = taxing_context.postal_code
    api_url = settings.AVA_API_URL
    api_url = api_url.format(postal_code, settings.AVA_API_KEY)

    ava_response = requests.get(api_url)
    if ava_response.status_code == '200':
        rate = ava_response.json()['totalRate']
    else:
        rate = 0

    tax = Tax()
    tax.rate = rate
    # tax.translations = taxing_context.region_code
    taxes = LineTax.from_tax(tax, base_price)

    taxful_price = TaxfulPrice(taxes.calcuate_amount(base_price))

    return TaxedPrice(taxful_price, base_price, taxes=taxes)
