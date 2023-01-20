from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# class CustomUserCreateForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("first_name", "last_name", 'username', 'email', "image")

class CustomUserCreateForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'firstname1',
            'placeholder': 'Enter first name'
        }
        )
    )

    last_name = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'last_name',
        'placeholder': 'Enter last name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'firstname1',
        'placeholder': 'Enter username'
    }))

    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={

        'class': 'firstname1', 'placeholder': 'Enter Email'
    }))

    image = forms.ImageField(widget=forms.FileInput(attrs={


    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'firstname1',
        'placeholder': 'Enter password'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'firstname1',
        'placeholder': 'comfirm password'
    }))

    class Meta:
        model = CustomUser
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  "image",
                  "password1",
                  "password2")

    # widgets = {
    #     'first_name': forms.TextInput(attrs={'class': 'firstname1', 'placeholder': 'Enter first name'}),
        # 'username': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
        # # 'image': forms.FileInput(attrs={'class': 'form-control'}),
        # 'user': forms.Select(attrs={'class': 'form-control'}),
    # }

    def save(self, commit=True):
        user = super(CustomUserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name",
                  'username', 'bio', 'email', "image")


# from django.contrib.auth.models import User


# Create your forms here.
