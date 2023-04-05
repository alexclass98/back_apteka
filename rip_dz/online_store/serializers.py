from .models import Drugs, Order, AuthUser
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
     class Meta:
         model = Drugs
         fields = ['price', 'name']




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Order
        # Поля, которые мы сериализуем
        fields = ["pk",  "product", "auth_user", "quantity", "price", "address", "status", "number_of_order", "date_of_delivery", "is_provider"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = AuthUser
        # Поля, которые мы сериализуем
        fields = ["pk",  "password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", "tel", "money"]