from django.contrib import admin
from . models import Invoice , Customer , Order , Payments

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Payments)
