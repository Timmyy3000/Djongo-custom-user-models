from django.contrib import admin
from .models import Customer
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, UserAdminCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['username', 'email', 'admin']
    list_filter = ['admin', 'staff', 'active']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password', 'password_2')}
        ),
    )
    search_fields = ['username', 'email']
    ordering = ['username', 'email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

class CustomerAdmin(admin.ModelAdmin):

    search_fields = ['username']
    class Meta:
        model = User

admin.site.register(Customer, CustomerAdmin)
