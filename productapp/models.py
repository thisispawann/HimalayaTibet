from django.db import models
from umapp.models import *


# Create your models here.

class Category(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to="category", null=True, blank=True)
    banner = models.ImageField(
        upload_to="category/banner/", null=True, blank=True)
    root = models.ForeignKey("self", on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        return self.title


class Product(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    product_code = models.CharField(
        max_length=20, unique=True, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    display_image = models.ImageField(upload_to="products/products/")
    meta_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    return_policy = models.TextField(default="Can not be returned")
    warranty = models.CharField(max_length=300, default="No warranty")
    on_sale = models.BooleanField(default=False, null=True, blank=True)
    is_featured = models.BooleanField(default=False, null=True, blank=True)
    marked_price = models.DecimalField(max_digits=19, decimal_places=2)
    selling_price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.title
    

class ProductImage(TimeStamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/image/")
    
    def __str__(self):
        return f"{self.product} ({self.id})"



class WishList(TimeStamp):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="wproduct")

    def __str__(self):
        return self.customer.user.username


class ProductReview(TimeStamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    text = models.TextField()

    def __str__(self):
        return f"By: ({self.customer}) for ({self.product})."
    

class Collection(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="collections")
    provide_discount = models.BooleanField(default=False)
    discount_pct = models.PositiveIntegerField(default=0)

    # def productimage(self):
    #     return self.collectionproduct_set.filter()[:3]

    def __str__(self):
        return self.title


class CollectionProduct(TimeStamp):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.collection.title + "(" + self.product.title + ")"