from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('Login/', views.login, name='login'),
    path('Register/', views.register, name='register'),
    path('ForgotPassword/', views.forgotpassword, name='forgot password'),
]