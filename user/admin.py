from django.contrib import admin
# from user import models

from .models import Registration

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","password")
    search_fields=("first_name","last_name","email","password")
admin.site.register(Registration,RegistrationAdmin)
