from django.db import models
from umapp.models import *
from productapp.models import Product
from django.utils.text import slugify


# Create your models here.

class OrganizationInformation(TimeStamp):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="organization")
    profile_image = models.ImageField(upload_to="organization", null=True, blank=True)
    address = models.CharField(max_length=500)
    slogan = models.CharField(max_length=500, null=True, blank=True)
    contact_no = models.CharField(max_length=200)
    alt_contact_no = models.CharField(max_length=200, null=True, blank=True)
    map_location = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    alt_email = models.EmailField(null=True, blank=True)
    about_us = models.TextField()
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.CharField(max_length=200, null=True, blank=True)
    viber = models.CharField(max_length=200, null=True, blank=True)
    seller_policy = models.TextField()
    return_policy = models.TextField()
    support_policy = models.TextField()
    privacy_policy = models.TextField()
    terms_conditions = models.TextField()
    return_policy_for_products = models.TextField(null=True, blank=True)
    meta_description = models.CharField(max_length=256, null=True, blank=True)
    fb_messenger_script = models.CharField(
        max_length=1024, null=True, blank=True)
    google_analytics_script = models.CharField(
        max_length=500, null=True, blank=True)
    fb_pixel_script = models.CharField(max_length=4000, null=True, blank=True)
    detail_pixel = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class PaymentMethod(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='payment_methods')
    merchant_code = models.CharField(max_length=50, null=True, blank=True)
    test_secret_key = models.CharField(max_length=1024, null=True, blank=True)
    live_secret_key = models.CharField(max_length=1024, null=True, blank=True)
    test_public_key = models.CharField(max_length=1024, null=True, blank=True)
    live_public_key = models.CharField(max_length=1024, null=True, blank=True)
    client_js_url = models.TextField(null=True, blank=True)
    test_api_endpoint = models.CharField(max_length=200, null=True, blank=True)
    live_api_endpoint = models.CharField(max_length=200, null=True, blank=True)
    client_config_script = models.TextField(null=True, blank=True)
    payment_url = models.CharField(max_length=200, null=True, blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Quotation(TimeStamp):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    email = models.EmailField()
    company = models.CharField(max_length=200, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    details = models.TextField()
    responded = models.BooleanField(default=False)

    def __str__(self):
    	return self.name + "(" + self.email + ")"
    

class QuotationReply(TimeStamp):
    quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"Return to: {self.quotation.email}"


class Cart(TimeStamp):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2)
    nettotal = models.DecimalField(max_digits=19, decimal_places=2)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def total_shipping_charge(self):
        total = 0
        for cp in self.cartproduct_set.all():
            total += cp.shipping_charge
        return total

    @property
    def total_charge(self):
        total_charge = self.nettotal + self.total_shipping_charge
        return total_charge


class CartProduct(TimeStamp):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=19, decimal_places=2)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    shipping_charge = models.PositiveIntegerField(default=50)
    order_status = models.CharField(
        max_length=200, choices=ORDER_STATUS, default='Pending')
    order_note = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Order(TimeStamp):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_code = models.CharField(
        max_length=200, unique=True, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    discount = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    shipping_charge = models.PositiveIntegerField(
        default=50, null=True, blank=True)
    shipping_charge_discount = models.PositiveIntegerField(
        default=0, null=True, blank=True)
    nettotal = models.DecimalField(max_digits=19, decimal_places=2)
    # payment_method = models.ForeignKey(
    #     PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    customer_payment_status = models.BooleanField(default=False)
    requested_shipping_date = models.DateField(null=True, blank=True)
    is_guest_checkout = models.BooleanField(default=False)
    # billing address
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, blank=True)
    street_address = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    order_status = models.CharField(
        max_length=200, choices=ORDER_STATUS, default='Pending')
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Payment(TimeStamp):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    tender = models.DecimalField(max_digits=19, decimal_places=2)
    change = models.DecimalField(max_digits=19, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.order.order_code


class Slider(TimeStamp):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="sliders")
    action_link_name = models.CharField(max_length=200, null=True, blank=True)
    action_link = models.CharField(max_length=200, null=True, blank=True)
    caption = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Blog(TimeStamp):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="blog")
    content = models.TextField()
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=1024, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Message(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=500, null=True, blank=True)
    description=models.TextField()
    contact_no = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length = 200, null=True, blank=True)

    def __str__(self):
        return self.name


class Faq(TimeStamp):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    def __str__(self):
        return self.question