from django.conf.urls import url
from . import views
from django.conf import settings # Подключаем settings.py
from django.conf.urls.static import static #Тут мы подключаем статику


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)