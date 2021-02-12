from django.urls import path
from .views import *


app_name = "umapp"
urlpatterns = [
    path("ecomm-admin/dashboard/",
        EcommAdminDashboard.as_view(), name="admindashboard"),
    path("ecomm-admin/",
        EcommAdminSigninView.as_view(), name="adminsignin"),
    path('ecomm-admin/signout/',
        EcommAdminSignoutView.as_view(), name="adminsignout"),
    
    # slider
    path("ecomm-admin/slider/list/",
        EcommAdminSliderListView.as_view(), name="adminsliderlist"),
	path('ecomm-admin/slider/create/', 
		EcommAdminSliderCreateView.as_view(), name='adminslidercreate'),
	path('ecomm-admin/slider/<int:pk>/update/', 
		EcommAdminSliderUpdateView.as_view(), name='adminsliderupdate'),
	path('ecomm-admin/slider/<int:pk>/delete/', 
		EcommAdminSliderDeleteView.as_view(), name='adminsliderdelete'),
	path('ecomm-admin/slider/<int:pk>/detail/', 
		EcommAdminSliderDetailView.as_view(), name='adminsliderdetail'),
]