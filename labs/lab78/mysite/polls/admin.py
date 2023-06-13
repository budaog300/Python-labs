from django.contrib import admin

from .models import Cashier, Store, Check, Sale, Item

admin.site.register(Cashier)
admin.site.register(Store)
admin.site.register(Check)
admin.site.register(Sale)
admin.site.register(Item)
