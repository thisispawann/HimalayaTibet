from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self, request):
        context = {}
        return render(request,'usertemplates/index.html',context)

class BlogView(View):
    def get(self, request):
        context = {}
        return render(request,'usertemplates/blog_page/blog.html',context)


class BlogDeatilView(View):
    def get(self, request):
        context = {}
        return render(request,'usertemplates/blog_page/blogDetails.html',context)


class ShopView(View):
    def get(self, request):
        context = {}
        return render(request,'usertemplates/shop_page/shop.html',context)
