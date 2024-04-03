from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    
    path("register/",views.RegisterView.as_view(),name="register"),
    #path("sendmail/",views.sendMail,name="sendmail"),
    path("dashboard/",views.DashboardView.as_view(),name="dashboard"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),
    path('Profile/', views.Profile, name='Profile'),
    path('contact/',views.contact, name='contact'),
    path('Features/',views.Features, name='Features'),
    path("Home/",views.Home, name="Home"),
    

    
]
