from django.contrib import admin
from .models import *

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'author',
        'pages',
        'price',
        'length',
        'width',
        'height',
        'front_cover',
        'back_cover',
        'spine',
        'properties',
        'created_at',
    ]
    list_display_links = ['slug']
    list_filter = ['created_at']
    # list_editable = []
    prepopulated_fields = {
        "slug": ["title"]
    }

