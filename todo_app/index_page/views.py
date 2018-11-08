from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ChunkModel
from .import forms


# Create your views here.
def index(request):
    chunkItems = ChunkModel.objects.order_by('id')
    addChunkForm = forms.AddChunkForm()
    ctx = {
        'chunkItems': chunkItems,
        'addForm': addChunkForm
    }
    return render(request, 'index_page/index.html', ctx)

@require_POST
def addChunk(request):
    form = forms.AddChunkForm(request.POST)
    if form.is_valid():
        newChunk = form.save(commit=False)
        newChunk.save()

    return redirect('index')
