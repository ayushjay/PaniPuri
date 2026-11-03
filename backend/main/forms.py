from django import forms
from .models import UserInputModel
from django.core.validators import MinLengthValidator


class UserInputForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = UserInputModel
        fields = "__all__"
