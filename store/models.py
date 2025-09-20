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
    Stores a single product entry related to :model:`store.category` and
    :model:`store.tags`
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


class Review(models.Model):
    """
    Stores a single review entry,
    related to :model:`auth.User` and :model:`store.Product`
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="reviews"
    )
    comment = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


class Order(models.Model):
    """
    Stores an instance of a user completing a purchase,
    related to :model:`store.OrderItem`
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="Pending")


class OrderItem(models.Model):
    """
    Stores an item which a user has successfully purchased,
    related to :model:`store.Order` and :model:`store.Product`
    """

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
