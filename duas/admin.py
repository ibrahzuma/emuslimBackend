from django.contrib import admin
from .models import Category, Dua

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Dua)
class DuaAdmin(admin.ModelAdmin):
    list_display = ('short_name_en', 'category', 'short_name_ar')
    list_filter = ('category',)
    search_fields = ('short_name_en', 'short_name_ar', 'full_dua_en')
