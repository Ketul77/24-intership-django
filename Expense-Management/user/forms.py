from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction



class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'Firstname', 'Lastname','password1', 'password2']
        
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user


