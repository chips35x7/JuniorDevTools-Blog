from django.contrib import admin
from django.contrib.auth import get_user_model
from pages.models import FeedBack


users = get_user_model()

class UserTabularInline(admin.TabularInline):
    model = FeedBack
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = [UserTabularInline,]

    list_display = [
        'username',
        'email',
        'is_superuser',
        'is_staff',
        'is_active'
    ]


admin.site.register(users, UserAdmin)