from django.contrib import admin
from .models import hotel, resort, hotel_detail, resort_detail, desc,rats,price,tora,address
# Register your models here.

admin.site.register(hotel)
admin.site.register(hotel_detail)
admin.site.register(resort)
admin.site.register(resort_detail)
admin.site.register(desc)
admin.site.register(rats)
admin.site.register(price)
admin.site.register(tora)
admin.site.register(address)