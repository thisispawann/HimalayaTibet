from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([
    OrganizationInformation, PaymentMethod, Quotation, QuotationReply, Cart, 
    CartProduct, Order, Payment, Slider, Blog, Message, Faq
    ])
