from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from hijack.contrib.admin import HijackUserAdminMixin

from .models import Dog


class DogAdmin(HijackUserAdminMixin, admin.ModelAdmin):
    list_display = ("name", "age")


# Define a new User admin
class UserAdmin(HijackUserAdminMixin, BaseUserAdmin):
    list_display = ("email", "first_name")
    pass


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Dog, DogAdmin)
