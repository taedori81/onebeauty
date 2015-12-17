from shoop.front.views.category import CategoryView as CoreCategoryView
from shoop.core.models import Product


class CategoryView(CoreCategoryView):

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        pass

