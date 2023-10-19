from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Создайте модель для запоминания бросков монеты:
# орёл или решка.
# Также запоминайте время броска.

# Доработаем задачу 1. 
# Добавьте статический метод для статистики по n последним броскам монеты. 
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.


class SaveCoin(models.Model):
    coin = (("О", "Орёл"), ("Р", "Решка"))
    coin_variant = models.CharField(max_length=1, choices=coin)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.coin_variant}  "

    class Meta:
        ordering = ["-date"]
    
    @staticmethod 
    def statistics(n):
        print(SaveCoin.objects.all()) 
        return SaveCoin.objects.all()[:n]