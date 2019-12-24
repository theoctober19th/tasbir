from django import forms
from .models import UserModel

class RegisterForm(forms.ModelForm):
    display_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'login__input',
                'placeholder' : 'Name',
                'name': 'display_name',
                'type': 'text',
            }
        )
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'login__input',
                'placeholder' : 'Username',
                'name': 'username',
                'type': 'text',
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'login__input',
                'placeholder' : 'Password',
                'name': 'password',
                'type': 'password',
            }
        )
    )

    email = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'login__input',
                'placeholder' : 'Email',
                'name': 'email',
                'type': 'email',
            }
        )
    )

    class Meta:
        model = UserModel
        fields = (
            'display_name',
            'password',
            'username',
            'email'
        )


class EditProfileForm(forms.ModelForm):

    display_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'edit-profile__input',
                'name': 'display_name',
                'type': 'text',
            }
        )
    )

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'edit-profile__input',
                'name': 'username',
                'type': 'text',
            }
        )
    )

    email = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'edit-profile__input',
                'name': 'email',
                'type': 'email',
            }
        )
    )

    website = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'edit-profile__input',
                'name': 'website',
                'type': 'text',
            }
        )
    )

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'edit-profile__input',
                'name': 'bio',
                'type': 'text',
            }
        )
    )

    profile_pic = forms.ImageField(
        required=False, 
    )
    
    class Meta:
        model = UserModel
        fields = (
            'display_name',
            'username',
            'bio',
            'website',
            'profile_pic',
            'email'
        )