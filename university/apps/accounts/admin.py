from django.contrib import admin

from university.apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
