from django.db import models

# Create your models here.
class CommonResource(models.Model):
    id = models.CharField(max_length = 50, unique = True, primary_key=True)
    #want this to be unique, but it can't b/c of the subresources
    title = models.CharField(max_length = 100)
    href = models.URLField() #unique = True)
    desc = models.TextField(blank=True)

    class Meta:
        abstract = True

class Resource(CommonResource): 
    pass

class Keyword(models.Model):
    word = models.CharField(max_length=100)
    resource = models.ForeignKey(Resource)

class SubResource(Resource):
    parent = models.ForeignKey(Resource, related_name="child")
