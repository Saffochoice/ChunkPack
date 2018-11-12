from django.db import models

# Create your models here.
class Badge(models.Model):
    text = models.CharField(max_length=10)
    color = models.CharField(max_length=7)
    def __str__(self):
        return self.text

class Language(models.Model):
    language = models.CharField(max_length=30)
    abb = models.CharField(max_length=10)
    color = models.CharField(max_length=7)
    def __str__(self):
        return self.language

class ChunkModel(models.Model):
    title = models.CharField(max_length=40)
    des = models.CharField(max_length=240)
    #badge = models.ForeignKey(Badge, on_delete=models.CASCADE, default='-')
    chunk = models.TextField(max_length=10000)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, default='-')
    def __str__(self):
        return self.pk
