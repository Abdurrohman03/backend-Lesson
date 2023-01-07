from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_deleted', 'modified_date', 'created_data']
    readonly_fields = ['modified_date', 'is_deleted', 'created_data']
    fields = ['title', 'image', 'content', 'modified_date', 'created_data']
    list_display_links = ['title', 'id']
    list_per_page = 10
    ordering = ['-id']
    search_fields = ['title']
    search_help_text = "'title' orqali qidiradi"
    list_filter = ['created_data', 'is_deleted', 'modified_date']
    date_hierarchy = 'created_data'


admin.site.register(Article, ArticleAdmin)
