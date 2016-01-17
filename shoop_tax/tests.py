from unittest import TestCase
from .module import get_tax_by_rate_and_postal_code, get_tax_rate_for_postal_code


class TaxModuleTest(TestCase):

    def test_get_tax_by_postal_code(self):
        rate = get_tax_rate_for_postal_code(90057)
        print(rate)