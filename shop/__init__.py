from shoop.apps import AppConfig
from shoop.addons.manager import add_enabled_addons


__all__ = ["add_enabled_addons"]


class ShopAppConfig(AppConfig):
    name = "shop"
    verbose_name = "One Beauty Shops"
    label = "shop"


default_app_config = "shop.ShopAppConfig"
