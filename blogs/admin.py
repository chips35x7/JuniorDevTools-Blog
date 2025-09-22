from django.contrib import admin
from .models import Blog, Comment, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'topic',
        'created_on'
    ]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Category)