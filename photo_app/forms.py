from django import forms
from .models import PhotoModel

class AddNewPostForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'edit-profile__input'
            }
        )
    )
    class Meta:
        model = PhotoModel
        fields = (
            'location',
            'photo'
        )