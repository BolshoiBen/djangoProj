from django.http import HttpResponse
from django.shortcuts import render

def firstPage(request):
    a='<h1>Hello World!</h1>'
    return render(request, '/index.html')