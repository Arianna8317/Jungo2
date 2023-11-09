from django.contrib import admin

# Register your models here.

from .models import Client, Product, Order, OrderProducts


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    ordering = ['name', '-price']
    list_filter = ['entering_date', 'price']
    search_fields = ['name']
    search_help_text = 'Поиск по полю  Название продукта (name)'


class OrderProductsAdmin(admin.ModelAdmin):
    actions = [reset_quantity]


admin.site.register(Client)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProducts, OrderProductsAdmin)
admin.site.register(Order)