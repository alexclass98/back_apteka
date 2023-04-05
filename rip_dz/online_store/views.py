from rest_framework import viewsets
from .serializers import DrugsSerializer, DrugsFilter, OrderSerializer, UserSerializer
from .models import Drugs, Order, AuthUser
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from rest_framework import permissions



class DrugsViewSet(viewsets.ModelViewSet):
    #Описание класса лекарств, добавляем тут сериалайзер и поля для фильтрации
    queryset = Drugs.objects.all()
    serializer_class = DrugsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DrugsFilter
    search_fields = [ '^name']
    # Сериализатор для модели
# Create your views here.



class OrderViewSet(viewsets.ModelViewSet):
    # Описание класса заказов, добавляем тут сериалайзер
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    # Описание класса пользователей, добавляем тут сериалайзер и поля для фильтрации
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer