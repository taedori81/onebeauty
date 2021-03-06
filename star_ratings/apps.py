from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete
from .models import UserRating
from .signals import calculate_ratings


class StarRatingsAppConfig(AppConfig):
    name = 'star_ratings'

    def ready(self):
        post_save.connect(calculate_ratings, sender=UserRating)
        post_delete.connect(calculate_ratings, sender=UserRating)
