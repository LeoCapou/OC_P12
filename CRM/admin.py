from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Client, Contrat, Event

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {"fields": ("username", "password", "is_sales", "is_support")})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
admin.site.register(Client)
admin.site.register(Contrat)
admin.site.register(Event)
