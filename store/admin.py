from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product, Review, Order, OrderItem, Category, Tag
from .forms import ProductAdminForm

# Register your models here.


class ProductAdmin(SummernoteModelAdmin):
    form = ProductAdminForm
    summernote_fields = ("description",)
    list_display = (
        "name",
        "price",
        "stock",
        "category",
        "published",
    )
    list_filter = (
        "published",
        "category",
        "tags",
    )
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("name",)}


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "rating",
        "approved",
    )
    list_filter = ("approved",)
    list_editable = ("approved",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Tag)
