from django.db import models

# Create your models here.
class Resource(models.Model):
   id = models.CharField(max_length = 50, unique = True)
   title = models.CharField(max_length = 100, unique = True)
   href = models.URLField(unique = True)

