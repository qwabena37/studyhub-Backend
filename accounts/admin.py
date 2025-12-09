from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your custom User model with the admin site
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Optional: customize fields shown in admin if you want
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('school', 'bio')}),
    )
