from django.shortcuts import render
from .models import Order

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html',{'object_list':object_list})

#Метод же POST, отправляет данные в теле запроса

def thank(request):
    #name = request.GET['name']  #GET Метод отправки формы
    #phone = request.GET['phone'] #Данные передается в строке браузера
    name = request.POST['name']  # POST
    phone = request.POST['phone']  #
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, './thanks_page.html', {'name': name,
                                                  'phone': phone})