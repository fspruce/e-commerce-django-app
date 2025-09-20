from django import forms
from .models import Product
from django_summernote.widgets import SummernoteWidget
from cloudinary.forms import CloudinaryFileField
from dal import autocomplete


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())
    image = CloudinaryFileField()

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "stock",
            "image",
            "slug",
            "category",
            "tags",
            "published",
        ]
        widgets = {
            "tags": autocomplete.ModelSelect2Multiple(url="tag-autocomplete"),
        }
