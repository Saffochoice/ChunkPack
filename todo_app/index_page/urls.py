from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addChunk', views.addChunk, name='addChunk'),
    path('languages', views.languages, name='languages'),
    path('editChunk/<id>', views.editChunk, name='editChunk'),
    path('single-chunk/<id>', views.singleChunk, name='singleChunk'),
]
