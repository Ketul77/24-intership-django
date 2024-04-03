from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import User 
from .forms import RegistrationForm
#import settings.py
from django.conf import settings
#send_mail is built-in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView,DetailView
from Expense.models import *
from django.db.models import Sum




# Create your views here.
class RegisterView(CreateView):
    template_name = 'user/register.html'
    model = User
    form_class = RegistrationForm
    success_url = '/user/login/'


    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
            

def sendMail(to):
    subject = 'Welcome to Expense Manager'
    message = 'You have successful register in Expense manager web Application'
    #recepientList = ["ketulsadat7@gmail.com"]
    recepientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    #attach file
    #html
    return True


class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user:
                return '/user/dashboard/'
            
            

class DashboardView(ListView):
    model = Expense

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate total sum of amounts
        total_amount = self.get_queryset().aggregate(Sum('amount'))['amount__sum']
        context['total_amount'] = total_amount if total_amount else 0
        return context
    
    def get(self, request, *args, **kwargs):
        context = {}
        expenses = Expense.objects.filter(user=self.request.user)
        labels = [expense.category.name for expense in expenses]
        data = [float(expense.amount) for expense in expenses]
        return render(request, 'user/dashboard.html',{
            "data":data,
            "labels":labels
        })
    
    
    template_name = 'user/dashboard.html'





class ProfileListView(ListView):
    model = User
    template_name = 'user/Profile.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset().filter(username=user.username)  # Filter by username or any other relevant field
        return queryset
    
    
@login_required
def contact(request):
    # Your view logic here
    return render(request, 'user/contact.html')

def Features(request):
    return render(request,'user/Features.html') 

def Home(request):
    return render(request,'user/Home.html')