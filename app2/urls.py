from django.urls import path
from app2 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('client_orders/<int:client_id>', views.client_orders, name='client_orders'),
    path('order_view/<int:order_id>', views.order_view, name='order_view'),
    path('client_orders_filtered/<int:client_id>/<int:days_ago>', views.client_orders_filtered,                            name='client_orders_filtered'),
    path('upload/', views.upload_image, name='upload_image'),
    path('product/', views.add_product, name='add_product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)