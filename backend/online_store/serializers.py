from .models import Drugs, Order, AuthUser, OrderOfProvider, Provisors
from rest_framework import serializers
from django_filters import rest_framework as filters




class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Drugs
        # Поля, которые мы сериализуем
        fields = ["pk",  "name", "description", "price", "amount", "category", "active_substance", "for_children", "img"]


#Фильтр по максимальным и минимальным значениям
class NumFilterMinMaxFilter(filters.BaseInFilter, filters.NumberFilter, filters.CharFilter):
    pass

class DrugsFilter(filters.FilterSet):

     pass
     max_pr = filters.NumberFilter(field_name='price', lookup_expr='lte')
     min_pr = filters.NumberFilter(field_name='price', lookup_expr='gte')
     search = filters.CharFilter(field_name='name', lookup_expr='icontains')
     search = filters.CharFilter(field_name='category', lookup_expr='icontains')
     class Meta:
         model = Drugs
         fields = ['price', 'name', 'category', 'active_substance']




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Order
        # Поля, которые мы сериализуем
        fields = ["pk",  "product", "auth_user", "quantity", "price", "address", "status", "number_of_order", "date_of_delivery", "date_made", "delivery_mode", "provisor_id"]

class OrderFilter(filters.FilterSet):
    pass
    search = filters.NumberFilter(field_name='product')
    search = filters.NumberFilter(field_name='number_of_order')
    search = filters.NumberFilter(field_name='auth_user')
    search = filters.NumberFilter(field_name='provisor_id')

    class Meta:
        model = Order
        fields = ["product", "number_of_order", "auth_user", "provisor_id"]


class OrderOfProviderSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = OrderOfProvider
        # Поля, которые мы сериализуем
        fields = ["pk", "number_of_order", "provider", "product", "price", "quantity", "status", "address",  "date_of_delivery", "date_made", "delivery_mode"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = AuthUser
        # Поля, которые мы сериализуем
        fields = ["pk",  "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", "tel", "balance",'address']


class ProvisorsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Provisors
        # Поля, которые мы сериализуем
        fields = ["pk",  "provisor", "address", "contact_tel", "img"]
