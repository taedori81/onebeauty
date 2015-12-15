from django.db import models
from shoop.core import models as shoop_models


class MyProduct(models.Model):
    product = models.OneToOneField(shoop_models.Product)

    def secondary_image(self):
        return "Secondary image"
