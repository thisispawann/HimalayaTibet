from django.urls import path
from .views import *


app_name = "ecomapp"

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('blog/', BlogView.as_view(),name='blog'),
    path('blog-detail/', BlogDeatilView.as_view(),name='blog-detail'),
    path('shop/', ShopView.as_view(),name='shop'),
]