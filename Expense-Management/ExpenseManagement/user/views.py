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



# Create your views here.
class RegisterView(CreateView):
    template_name = 'user/register.html'
    model = User
    form_class = RegistrationForm
    success_url = '/login'


    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
            

def sendMail(to):
    subject = 'Welcome to PMS24'
    message = 'Hope you are enjoying your Django Tutorials'
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
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/dashboard.html')
    
    
    template_name = 'user/dashboard.html'






@login_required
def Profile(request):
    myuser=User.objects.all()
    # print(myuser.username)
    return render(request, 'user/Profile.html',{'context':myuser})


def contact(request):
    # Your view logic here
    return render(request, 'user/contact.html')

def Features(request):
    return render(request,'user/Features.html') 

def Home(request):
    return render(request,'user/Home.html')