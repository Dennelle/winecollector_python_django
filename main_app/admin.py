from django.contrib import admin

from .models import Wine, Drinking, Country

# Register your models here.
admin.site.register(Wine)
admin.site.register(Drinking)
admin.site.register(Country)
