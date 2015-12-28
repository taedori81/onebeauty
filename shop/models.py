from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from shoop.core import models as shoop_models
from shoop.core.models import Shop, Product


class MyProduct(models.Model):
    product = models.OneToOneField(shoop_models.Product, on_delete=models.CASCADE)

    def secondary_image(self):
        shop = Shop.objects.first()
        product = self.product
        shop_product = product.get_shop_instance(shop)
        images = list(shop_product.images.all())
        if len(images) > 1:
            secondary_image = images[1]
        else:
            secondary_image = images[0]
        return secondary_image

    def all_images(self):
        shop = Shop.objects.first()
        product = self.product
        shop_product = product.get_shop_instance(shop)
        images = list(shop_product.images.all())
        return images


def create_myproduct(sender, instance, created, **kwargs):
    """Create MyProduct class for every new Product"""
    if created:
        MyProduct.objects.create(product=instance)

signals.post_save.connect(create_myproduct, sender=Product, weak=False,
                          dispatch_uid='models.create_myproduct')
