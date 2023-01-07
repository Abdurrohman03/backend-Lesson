from django.contrib import admin
from .models import *


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )
    list_display = ('id', 'author', 'title', 'is_active', 'craeted_date')
    search_fields = ('title', )
    list_filter = ('is_active', 'tags')
    date_hierarchy = 'craeted_date'
    filter_horizontal = ('tags', )
    autocomplete_fields = ('author', )


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_author', 'recipe', 'title', 'quantity', 'unit', 'craeted_date')
    date_hierarchy = 'craeted_date'
    autocomplete_fields = ('recipe', )
    list_filter = ('unit', )
    search_fields = ('title', 'recipe__title')


admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

