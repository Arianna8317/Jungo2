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
    image = models.ImageField(upload_to=None)
    #quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Product name: {self.name}, price: {self.price}, description: {self.description}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

class OrderProducts (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()