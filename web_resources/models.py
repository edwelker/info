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

    def __unicode__(self):
        return u'%s' % (self.title)

class Resource(CommonResource): 
    pass

class Keyword(models.Model):
    word = models.CharField(max_length=100)
    resource = models.ForeignKey(Resource)

    def __unicode__(self):
        return u'%s' % (self.word)

class SubResource(Resource):
    parent = models.ForeignKey(Resource, related_name="child")

class Category(models.Model):
    id = models.CharField(max_length=30, unique=True, primary_key=True)
    display_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
