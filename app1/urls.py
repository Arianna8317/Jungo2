from django.urls import path
from app1 import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('last_coin/', views.last_coin, name='last_coin'),
]