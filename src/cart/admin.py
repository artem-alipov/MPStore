from django.contrib import admin

# Register your models here.
from .models import Cart, BookInOrder, Order

admin.site.register(BookInOrder)
admin.site.register(Order)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_total_price"
    )