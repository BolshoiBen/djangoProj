from django.db import models

# Create your models here.
#здесь опичываются таблички базы данных
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name=models.CharField(max_length=200)
    order_phone=models.CharField(max_length=200)

'''
Работа с моделями в консоли

    python manage.py shell #открыть консоль
        from crm.models import Order #импорт ордер
        n=Order(order_name = "Иван",order_phone="+79372285927") #присваивание переменной
        n.save() #добавление переменной в список бд
        from django.db import connection
        connection.queries
        n3 = order.objects.create(order_name = 'bob', order_phone = '+7355558383')
        Order.objects.all()
        Order.objects.create(order_name = 'bob', order_phone = '+7353531861')
        Order.objects.filter(order_name= "bob"
        Order.objects.objects.order_by('id')
        Order.objects.objects.order_by('-id')
        Order.objects.get(pk=1)
            Order.objects.get(id=1)
                Order.objects.get(order_name="bob") #ошибка
                Order.objects.get(pk=55) #ошибка
        order1=Order.objects.get(pk=1)
        order1.order_phone
        order1.order_dt
        order1.order_phone = '23232'
        order1.save()
'''