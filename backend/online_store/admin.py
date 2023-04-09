from django.contrib import admin
# Register your models here.
from .models import Order, Drugs, OrderOfProvider, Provisors

#Описание администратора, добавляем ему таблицы, к которым есть доступ
admin.site.register(Drugs)
admin.site.register(Order)
admin.site.register(OrderOfProvider)
admin.site.register(Provisors)
