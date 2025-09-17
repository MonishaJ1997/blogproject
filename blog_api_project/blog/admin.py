from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'view_count', 'created_at')
    list_filter = ('author', 'category', 'created_at')
    search_fields = ('title', 'content', 'category', 'tags')
