from django.shortcuts import render
from django.http import HttpResponse

def retornar2(request):
    return render(request, 'index.html')
