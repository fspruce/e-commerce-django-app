from django.urls import path
from . import views
from .views import ProductList, TagAutocomplete


urlpatterns = [
    path("", ProductList.as_view(), name="home"),
    path("<slug:slug>/", views.product_detail, name="product_detail"),
    path("tag-autocomplete/", TagAutocomplete.as_view(), name="tag-autocomplete"),
]
