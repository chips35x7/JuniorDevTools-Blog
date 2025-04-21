from django.contrib import admin
from django.contrib.auth import get_user_model


users = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'is_superuser',
        'is_staff'
    ]


admin.site.register(users, UserAdmin)