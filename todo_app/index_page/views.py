from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ChunkModel, Language
from .import forms


# Create your views here.
def index(request):
    chunkItems = ChunkModel.objects.order_by('id')


    #a = ChunkModel.objects.get(pk=8)
    #addChunkForm = forms.AddChunkForm(instance=a)
    addChunkForm = forms.AddChunkForm()
    ctx = {
        'chunkItems': chunkItems,
        'addForm': addChunkForm
    }
    return render(request, 'index_page/index.html', ctx)

def languages(request):
    langItems = Language.objects.order_by('id')
    addLangForm = forms.AddLangForm()
    ctx = {
        'langItems': langItems,
        'addForm': addLangForm
    }
    return render(request, 'index_page/languages.html', ctx)


def singleChunk(request, id):
    chunkItem = ChunkModel.objects.get(pk=id)
    editChunkForm = forms.EditChunkForm(instance=chunkItem)
    addChunkForm = forms.AddChunkForm()
    ctx = {
        'chunkItem': chunkItem,
        'addForm': addChunkForm,
        'editForm': editChunkForm,
    }
    return render(request, 'index_page/single-page.html', ctx)

@require_POST
def addChunk(request):
    form = forms.AddChunkForm(request.POST)
    if form.is_valid():
        newChunk = form.save(commit=False)
        newChunk.save()

    return redirect('index')
@require_POST
def editChunk(request, id):
    form = forms.EditChunkForm(request.POST)
    if form.is_valid():
        chunkItem = ChunkModel.objects.get(pk=id)
        form= forms.EditChunkForm(request.POST, instance=chunkItem)
        #newChunk = form.save(commit=False)
        form.save()

    return redirect('../single-chunk/{0}'.format(id))
