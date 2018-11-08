from django import forms
from django.forms import ModelForm
from . import models

class AddChunkForm(ModelForm):
    class Meta:
        model = models.ChunkModel
        fields = ['title', 'des', 'badge', 'chunk', 'lang']
