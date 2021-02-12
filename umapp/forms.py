from django import forms
from .models import *
from ecomapp.models import Slider
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SigninForm(forms.Form):
	username = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'style_input',
			'placeholder': 'Enter Username'
			}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'class': 'style_input',
			'placeholder': 'Enter Password'
			}))


class SliderForm(forms.ModelForm):
	class Meta:
		model = Slider
		fields = "__all__"
		widgets = {
		'title': forms.TextInput(attrs={
			'class': 'form-control form-control-rounded',
			'placeholder': 'Enter Title',
			}),
		'image': forms.ClearableFileInput(attrs={
			'class': 'form-control form-control-rounded',
			'accept': 'image/*',
			}),
		'content': SummernoteWidget(attrs={
				'summernote': {
					'class': 'form-control form-control-rounded',
					'placeholder': 'Enter Content',
					'height': '400px'
				}
			}),
		'action_link_name': forms.TextInput(attrs={
			'class': 'form-control form-control-rounded',
			'placeholder': 'Enter Link Name',
			}),
		'action_link': forms.TextInput(attrs={
			'class': 'form-control form-control-rounded',
			'placeholder': 'Enter link to redirect'
			}),
		}
