from django.contrib import admin
from online_store import views as all_views
from django.urls import include, path, re_path
from rest_framework import routers
from django.conf.urls import include

#Описание ссылок, по которым доступна информация из таблица

#Объединение таблиц в группу
from django.views.generic import TemplateView
router = routers.DefaultRouter()
router.register(r'drugs', all_views.DrugsViewSet)
router.register(r'order', all_views.OrderViewSet)
router.register(r'user', all_views.UserViewSet)





# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#Паттерны ссылок
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]