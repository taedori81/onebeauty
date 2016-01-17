from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.lru_cache import lru_cache

from shoop.core.taxing import TaxModule
from shoop.core.taxing.utils import stacked_value_added_taxes
from shoop.utils.i18n import format_percent

from shoop.core.models import Tax
from shoop.core.pricing import TaxfulPrice, TaxlessPrice
from shoop.core.taxing import TaxedPrice, LineTax

import requests
from requests.exceptions import RequestException


class AvaTaxModule(TaxModule):

    identifier = "avalara_tax"
    name = _("Avalara Taxation")

    def get_taxed_price_for(self, context, item, price):
        tax = get_tax(context.postal_code)
        return stacked_value_added_taxes(price, [tax])


@lru_cache()
def get_tax(postal_code):
    rate = get_tax_rate_for_postal_code(postal_code)
    return get_tax_by_rate_and_postal_code(rate, postal_code)


def get_tax_rate_for_postal_code(postal_code):
    api_url = settings.AVA_API_URL
    api_url = api_url.format(postal_code, settings.AVA_API_KEY)
    rate = 0.00
    try:
        ava_response = requests.get(api_url)
        if ava_response.status_code == 200:
            # Avalara return total rate in string like 9.0
            rate = ava_response.json()['totalRate']
            # Convert to float and change to like 0.09
            rate = float(rate) * 0.01

    except RequestException as e:
        print(e)

    return rate


def get_tax_by_rate_and_postal_code(rate, postal_code):
    code = '%s:%s' % (postal_code, rate)  # Note: rates for a postal code could change
    tax_data = {
        'name': _("%(percent)s tax for ZIP %(postal_code)s") % {
            'percent': format_percent(rate, 2), 'postal_code': postal_code,
        },
    }
    tax = Tax.objects.language('en').get_or_create(rate=rate, code=code, defaults=tax_data)[0]
    return tax
