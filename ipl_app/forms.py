from django import forms
from django.forms import ModelForm
from .models import temp_model


class TempForm(ModelForm):
    class Meta:
        model = temp_model
        fields = "__all__"

