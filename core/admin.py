from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category, Product, Stock, StockDetail, Sale, SaleDetail


class UserAdmin(BaseUserAdmin):
    """Custom user admin."""
    list_display = ('u_name', 'email', 'f_name', 'l_name', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('u_name', 'password')}),
        ('Personal info', {'fields': ('f_name', 'l_name', 'email', 'profile')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('u_name', 'email', 'f_name', 'l_name', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('u_name', 'email', 'f_name', 'l_name')
    ordering = ('-date_joined',)


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockDetail)
admin.site.register(Sale)
admin.site.register(SaleDetail)
