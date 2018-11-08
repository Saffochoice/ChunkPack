from django.db import models

# Create your models here.
class Badge(models.Model):
    text = models.CharField(max_length=10)
    color = models.CharField(max_length=7)
    def __str__(self):
        return self.text

class ChunkModel(models.Model):
    title = models.CharField(max_length=40)
    des = models.CharField(max_length=240)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, default='-')
    chunk = models.TextField(max_length=10000)
    lang = models.CharField(max_length=30)
    def __str__(self):
        return self.title
