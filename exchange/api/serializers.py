from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
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
        )
