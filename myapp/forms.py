from django import forms
from .models import Input
from django.db import models


class Messages(forms.ModelForm):
    class Meta:
        model = Input
        fields = ('sentence','document' )

