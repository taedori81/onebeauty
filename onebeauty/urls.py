"""onebeauty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import set_language


urlpatterns = patterns(
    '',
    url(r'^set-language/', set_language, name="set-language"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sa/', include('shoop.admin.urls', namespace="shoop_admin", app_name="shoop_admin")),
    url(r'^api/', include('shoop.api.urls')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^', include('shoop.front.urls', namespace="shoop", app_name="shoop")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

