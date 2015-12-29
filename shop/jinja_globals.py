from django_jinja import library
from shoop.front.template_helpers.general import _get_list_products
from shoop.core.models import Product
from jinja2.utils import contextfunction


def get_product_by_id(product_id):
    return Product.objects.all().filter("pk" == product_id)


library.global_function("get_product_by_id", get_product_by_id)
