from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')
    list_filter = ('published', 'created')
