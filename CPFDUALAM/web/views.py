from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return HttpResponse("This the login page")

def register(request):
    return HttpResponse("This the register page")

def forgotpassword(request):
    return HttpResponse("This the forgot password page")

def account(request):
    return HttpResponse("This the account page")