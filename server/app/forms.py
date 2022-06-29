from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm
from django.db import models
from .models import *


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'