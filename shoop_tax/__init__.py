from shoop.apps import AppConfig


class ShoopTaxAppConfig(AppConfig):
    name = "shoop_tax"
    verbose_name = "Shoop Tax Checkout integration"
    label = "shoop-tax"
    provides = {
        "tax_module": ["shoop_tax.module:AvaTaxModule"]
    }


default_app_config = "shoop_tax.ShoopTaxAppConfig"

