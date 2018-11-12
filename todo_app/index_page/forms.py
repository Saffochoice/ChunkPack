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

class AddLangForm(ModelForm):
    class Meta:
        model = models.Language
        fields = ['language', 'abb', 'color']
        widgets = {
            'language': TextInput(attrs={'class':'input-text__element'}),
            'abb': TextInput(attrs={'class':'input-text__element'}),
            'color': TextInput(attrs={'class':'input-text__element'}),
        }
        
class EditChunkForm(ModelForm):
    class Meta:
        model = models.ChunkModel
        fields = ['title', 'des', 'chunk', 'lang']
        widgets = {
            'title': TextInput(attrs={'class':'input-text__element'}),
            'des': TextInput(attrs={'class':'input-text__element'}),
            #'lang': SelectMultiple(attrs={'class':'select__element'}),
            'chunk': Textarea(attrs={'class':'textarea__element'}),
        }
