# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product, OrderProducts
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ProductForm, ImageForm
import logging
from django.db.models import Sum

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("This is the about page.")


def client_orders(request, client_id):
    client= get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    return render(request, "app2/client_orders.html", {'client': client, 'orders': orders})


def client_orders_filtered(request, client_id, days_ago):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(date_ordered__gt=datetime.now()-timedelta(days=days_ago))
    orders = orders.filter(customer=client_id)
    return render(request, "app2/client_orders.html", {'client': client, 'orders': orders})


def order_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    orderproducts = OrderProducts.objects.filter(order=order)
    return render(request, "app2/order_view.html", {'order': order, 'orderproducts': orderproducts})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ProductForm()
    return render(request, 'app2/upload_image.html', {'form':  form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            entering_date = form.cleaned_data['entering_date']
            product = Product(name=name, price=price, description=description, entering_date=entering_date, image=image)
            product.save()
            message = 'Пользователь сохранён'
        message = form.errors
        return render(request, 'app2/product_inform.html', {'message': message})
    
    else:
        form = ProductForm()
        message = 'Заполните карточку товара'
        return render(request, 'app2/edit_products_form.html', {'form': form, 'message': message})
    

def total_in_db(request):
    total = Product.objects.aggregate(Sum('price'))
    context = {
        'title': 'Общая цена товаров в каталоге -  посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)
