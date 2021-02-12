from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import JsonResponse
from ecomapp.models import OrganizationInformation

from .forms import *


# Create your views here.
class AdminRequiredMixin(SuccessMessageMixin, object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('umapp:adminsignin')
        return super().dispatch(request, *args, **kwargs)

        return context


class EcommAdminSigninView(FormView):
    template_name = "admintemplates/adminsignin.html"
    form_class = SigninForm
    success_url = reverse_lazy('umapp:admindashboard')
    success_message = "Logged in Successfully"

    # to redirect to dashboard if already logged in
    def dispatch(self, request, *args, **kwargs):
    	if request.user.is_authenticated:
    		return redirect(self.success_url)
    	return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']

        data_password = form.cleaned_data['password']

        user = authenticate(username=username, password=data_password)

        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'errors': "User credentials didn't match"
            })
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['org'] = OrganizationalInformation.objects.first()

    #     return context


class EcommAdminSignoutView(View):
	def get(self, request, **kwargs):
		if request.user.is_authenticated:
			logout(request)
			return redirect("umapp:adminsignin")
		else:
			raise Http404


class EcommAdminDashboard(AdminRequiredMixin, TemplateView):
    template_name = "admintemplates/admindashboard.html"


# slider
class EcommAdminSliderListView(AdminRequiredMixin, TemplateView):
    template_name = "admintemplates/website/adminsliderlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        sliderlist = Slider.objects.all().order_by('-id')
        page = self.request.GET.get('page', 1)

        paginator = Paginator(sliderlist, 25)
        try:
            updates = paginator.page(page)
        except PageNotAnInteger:
            updates = paginator.page(1)
        except EmptyPage:
            updates = paginator.page(paginator.num_pages)
        context['sliderlist'] = updates

        return context


class EcommAdminSliderCreateView(AdminRequiredMixin, CreateView):
    template_name = 'admintemplates/website/adminslidercreate.html'
    form_class = SliderForm
    success_url = reverse_lazy('tphapp:adminsliderlist')
    success_message = " Slider Created Successfully!!!"

    def get_success_message(self, cleaned_data):
        title = cleaned_data['title']
        return title + self.success_message


class EcommAdminSliderUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'admintemplates/website/adminslidercreate.html'
    form_class = SliderForm
    model = Slider
    success_url = reverse_lazy('tphapp:adminsliderlist')
    success_message = " Slider Updated Successfully!!!"

    def get_success_message(self, cleaned_data):
        title = cleaned_data['title']
        return title + self.success_message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'

        return context


class EcommAdminSliderDeleteView(AdminRequiredMixin, DeleteView):
    template_name = 'admintemplates/website/adminsliderdelete.html'
    model = Slider
    success_url = reverse_lazy('tphapp:adminsliderlist')
    success_message = " Slider Deleted Successfully!!!"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, self.object.title + self.success_message)
        return super(AdminSliderDeleteView, self).delete(request, *args, **kwargs)


class EcommAdminSliderDetailView(AdminRequiredMixin, DetailView):
    template_name = 'admintemplates/website/adminsliderdetail.html'
    model = Slider
    context_object_name = 'sliderdetail'