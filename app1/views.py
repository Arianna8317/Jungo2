# Добавьте статический метод для статистики по n последним броскам монеты. 
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.from django.shortcuts import rende
# Create your views here.
from django.http import HttpResponse
import random
import logging


def coin(request):
    rnd_coin = random.choice(["Орёл", "Решка"])
    #save_coin = SaveCoin(coin_variant=rnd_coin)
    #save_coin.save()
    return HttpResponse(rnd_coin)


