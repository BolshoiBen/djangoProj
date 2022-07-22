from django.http import HttpResponse

def firstPage(request):
    return HttpResponse("Hello World!")