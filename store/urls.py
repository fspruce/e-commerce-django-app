from django.urls import path
from . import views
from .views import TagAutocomplete


urlpatterns = [
    path("", views.index, name="home"),
    path("tag-autocomplete/", TagAutocomplete.as_view(), name="tag-autocomplete"),
]
