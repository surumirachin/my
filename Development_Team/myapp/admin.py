from django.contrib import admin

from Development_Team.myapp.models import Customer, Order, Product, Tag

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)