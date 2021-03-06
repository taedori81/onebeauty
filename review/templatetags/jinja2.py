"""Template tags for the ``review`` app."""
from django.contrib.contenttypes.models import ContentType

from django_jinja import library

from .. import models


def get_reviews(obj):
    """Simply returns the reviews for an object."""
    ctype = ContentType.objects.get_for_model(obj)
    return models.Review.objects.filter(content_type=ctype, object_id=obj.id)


def get_review_average(obj):
    """Returns the review average for an object."""
    total = 0
    reviews = get_reviews(obj)
    if not reviews:
        return False
    for review in reviews:
        average = review.get_average_rating()
        if average:
            total += review.get_average_rating()
    if total > 0:
        return total / reviews.count()
    return False


def get_review_count(obj):
    """Simply returns the review count for an object."""
    return get_reviews(obj).count()


# @register.inclusion_tag('review/partials/category_averages.html')
def render_category_averages(obj, normalize_to=100):
    """Renders all the sub-averages for each category."""
    context = {'reviewed_item': obj}
    ctype = ContentType.objects.get_for_model(obj)
    reviews = models.Review.objects.filter(
        content_type=ctype, object_id=obj.id)
    category_averages = {}
    for review in reviews:
        review_category_averages = review.get_category_averages(normalize_to)
        for category, average in review_category_averages.iteritems():
            if category not in category_averages:
                category_averages[category] = review_category_averages[
                    category]
            else:
                category_averages[category] += review_category_averages[
                    category]
    if reviews and category_averages:
        for category, average in category_averages.items():
            category_averages[category] = \
                category_averages[category] / models.Rating.objects.filter(
                    category=category, value__isnull=False,
                    review__content_type=ctype, review__object_id=obj.id
                ).exclude(value='').count()
    else:
        category_averages = {}
        for category in models.RatingCategory.objects.filter(
                counts_for_average=True):
            category_averages[category] = 0.0
    context.update({'category_averages': category_averages})
    return context


def total_review_average(obj, normalize_to=100):
    """Returns the average for all reviews of the given object."""
    ctype = ContentType.objects.get_for_model(obj)
    total_average = 0
    reviews = models.Review.objects.filter(
        content_type=ctype, object_id=obj.id)
    for review in reviews:
        total_average += review.get_average_rating(normalize_to)
    if reviews:
        total_average /= reviews.count()
    return total_average


def user_has_reviewed(obj, user):
    """Returns True if the user has already reviewed the object."""
    ctype = ContentType.objects.get_for_model(obj)
    try:
       reviwed = models.Review.objects.get(user=user, content_type=ctype,
                                           object_id=obj.id)
    except models.Review.DoesNotExist:
        return False
    return True


def get_review_by_user(obj, user):
    ctype = ContentType.objects.get_for_model(obj)
    try:
        reviewed_item = models.Review.objects.get(user=user, content_type=ctype,
                                                  object_id=obj.id)
    except models.Review.DoesNotExist:
        return None
    return reviewed_item


from babel import dates


def format_datetime(value, format='medium'):
    if format == 'full':
        format = "EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format = "EE dd.MM.y HH:mm"
    return dates.format_datetime(value, format)


from shoop.core.models import Product


def get_product_by_id(product_id):
    return Product.objects.get(pk=product_id)

library.global_function("get_product_by_id", get_product_by_id)


library.global_function("user_has_reviewed", user_has_reviewed)
library.global_function("total_review_average", total_review_average)
library.global_function("get_review_count", get_review_count)
library.global_function("get_review_average", get_review_average)
library.global_function("get_reviews", get_reviews)
library.global_function("render_category_averages", render_category_averages)
library.global_function("get_review_by_user", get_review_by_user)


library.global_function("datetime", format_datetime)

