from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(ServiceProvider)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(CustomerMenuItem)
admin.site.register(Address)