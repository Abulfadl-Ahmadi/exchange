from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
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
        )

        widgets = {
            # 'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
            # # 'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'user': forms.Select(attrs={'class': 'form-control'}),
        }


# class PostForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Post
#         fields = ('title', 'content', 'image', 'user', 'slug')
