from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('rexchecker/', views.rexcheckerView, name='rexchecker'),
    path('login-demo/', views.loginView, name='login'),
    path('register-demo/', views.registerView, name='register'),
    path('byte-art/', views.byteArtView, name='byte-art'),
]
