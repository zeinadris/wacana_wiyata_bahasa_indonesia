from pyexpat import model
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title
