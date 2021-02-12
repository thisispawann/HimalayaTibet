from django.db import models
from django.contrib.auth.models import User, Group
from .constants import *
from django.utils import timezone

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        return super().save(*args, **kwargs)


class Region(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class City(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    default_shipping_charge = models.PositiveIntegerField(default=25)

    def __str__(self):
        return self.title
    


class EcommerceAdmin(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user/ecommerceadmin", null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        group, group_created = Group.objects.get_or_create(name="EcommerceAdmin")
        self.user.group.add(group)
        super().save(*args, **kwargs)


class Customer(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="user/customer", null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    street_address = models.CharField(max_length=200, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        group, group_create = Group.objects.get_or_create(name="Customer")
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Subscriber(TimeStamp):
    email = models.EmailField()

    def __str__(self):
        return self.email