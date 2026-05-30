<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
=======
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
>>>>>>> 32677c0ee0bba3b3a536a8c6177a6e7f80d801a8
        fields=['first_name','username','email','password']