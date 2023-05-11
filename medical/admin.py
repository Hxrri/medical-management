from django.contrib import admin
from .models import contact,product,Order
# Register your models here.
admin.site.register(contact)
admin.site.register(product)
admin.site.register(Order)