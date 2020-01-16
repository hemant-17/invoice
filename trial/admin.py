from django.contrib import admin
from . models import Invoice , Customer , Profile , Wallet

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Wallet)
