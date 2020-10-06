from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

'''
	CreateUserFOrm class describes a form and determines how it works and appears
	It has two main fields i.e username and email and password1, password2 are also defined as field through __init__
	Widgets are for the attributes required for the field such as type, class, placeholder etc.
'''

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email']

		widgets ={
			'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
		}
	
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Password"})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Repeat your password"})
