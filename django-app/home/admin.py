from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('published_date', 'created_date')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_date'
