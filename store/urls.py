from django.urls import path
from . import views
from .views import TagAutocomplete


urlpatterns = [
    path("", views.home_page_view, name="home"),
    path("tag-autocomplete/", TagAutocomplete.as_view(), name="tag-autocomplete"),
]
