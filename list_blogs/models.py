from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class ListBlog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc3 = models.TextField()
    desc5 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title