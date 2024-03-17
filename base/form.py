from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import User


class MyUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password']