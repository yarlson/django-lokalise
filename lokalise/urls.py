from django.conf.urls import url

from .views import hook

urlpatterns = [
    url(r'^hook$', hook),
]
