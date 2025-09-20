from django.db import models
from django.contrib.auth.models import User
from django_summernote.models import SummernoteTextField
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    """
    Stores a category of item related to :model:`store.Product`
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)


class Tag(models.Model):
    """
    Stores a tag entry related to :model:`store.Product`
    """

    name = models.CharField(max_length=50, unique=True)


class Product(models.Model):
    """
    Stores a single product entry
    """

    name = models.CharField(max_length=200)
    description = SummernoteTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    image = CloudinaryField("image")
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField("Tag", blank=True)
    published = models.BooleanField(default=False)
