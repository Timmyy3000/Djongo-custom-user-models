from django.contrib import admin
from .models import Customer
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()

class UserAdmin(admin.ModelAdmin):

    search_fields = ['username']
    class Meta:
        model = User

admin.site.register(User, UserAdmin)

class CustomerAdmin(admin.ModelAdmin):

    search_fields = ['username']
    class Meta:
        model = User

admin.site.register(Customer, CustomerAdmin)
