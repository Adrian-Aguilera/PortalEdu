from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def retornar(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def retornar2(request):
    return render(request, 'mesaje.html')

def template2(request):
    return render(request, 'template 2.html')
