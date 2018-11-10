from django import forms
from django.forms import ModelForm, TextInput, Textarea, SelectMultiple
from . import models

class AddChunkForm(ModelForm):
    class Meta:
        model = models.ChunkModel
        fields = ['title', 'des', 'chunk', 'lang']
        widgets = {
            'title': TextInput(attrs={'class':'input-text__element'}),
            'des': TextInput(attrs={'class':'input-text__element'}),
            #'lang': SelectMultiple(attrs={'class':'select__element'}),
            'chunk': Textarea(attrs={'class':'textarea__element'}),
        }
