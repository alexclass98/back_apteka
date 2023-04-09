from rest_framework import viewsets
from .serializers import DrugsSerializer, DrugsFilter, OrderSerializer, UserSerializer, \
    OrderOfProviderSerializer, OrderFilter, ProvisorsSerializer
from .models import Drugs, Order, AuthUser, OrderOfProvider, Provisors
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from rest_framework import permissions


class DrugsViewSet(viewsets.ModelViewSet):
    # Описание класса лекарств, добавляем тут сериалайзер и поля для фильтрации
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DrugsFilter
    search_fields = ['^name', '^category']
    # Сериализатор для модели


class OrderOfProviderViewSet(viewsets.ModelViewSet):
    # Описание класса заказов поставщика, добавляем тут сериалайзер
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = OrderOfProvider.objects.all()
    serializer_class = OrderOfProviderSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    # Описание класса заказов, добавляем тут сериалайзер
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter
    search_fields = ['^product', '^number_of_order', 'auth_user']
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    # Описание класса пользователей, добавляем тут сериалайзер и поля для фильтрации
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer


class ProvisorsViewSet(viewsets.ModelViewSet):
    # Описание класса пользователей, добавляем тут сериалайзер и поля для фильтрации
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Provisors.objects.all()
    serializer_class = ProvisorsSerializer
