from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f'Client name: {self.name}, email: {self.email}, address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    entering_date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Product name: {self.name}, price: {self.price}, quantity: {self.quantity}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    