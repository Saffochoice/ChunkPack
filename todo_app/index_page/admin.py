from django.contrib import admin

# Register your models here.
from .models import ChunkModel, Badge, Language

admin.site.register(ChunkModel)
admin.site.register(Badge)
admin.site.register(Language)
