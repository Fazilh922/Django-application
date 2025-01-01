from django.contrib import admin

# Register your models here.
from .models import Country, User, Blog

admin.site.register(Country)
admin.site.register(User)
admin.site.register(Blog)