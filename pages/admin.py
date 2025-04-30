from django.contrib import admin

from .models import FeedBack

class FeedBackAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'message',
        'created_on'
    ]

admin.site.register(FeedBack, FeedBackAdmin)