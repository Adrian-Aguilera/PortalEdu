from django.shortcuts import render
#from .models import login

# Create your views here.

def login(request):
    #user_all =login
    return render(request, "login.html")