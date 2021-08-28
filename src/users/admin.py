from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.
#@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('uid', 'password')}),
        (_('Personal info'), {'fields': ('displayname', 'photo_url')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('displayname', 'photo_url', 'is_staff', 'role')
    list_filter = ('is_staff', 'displayname')
    search_fields = ('displayname', 'photo_url')
    filter_horizontal = ('groups', 'user_permissions')
    ordering = ('uid',)