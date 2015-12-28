from shoop.apps import AppConfig
from shoop.addons.manager import add_enabled_addons


__all__ = ["add_enabled_addons"]


class ReviewAppConfig(AppConfig):
    name = "review"
    verbose_name = "Review app"
    label = "review"


default_app_config = "review.ReviewAppConfig"
