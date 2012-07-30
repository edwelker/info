from django.db import models

# Create your models here.
class Keyword(models.Model):
    word = models.CharField(max_length=100)
    resource = models.ForeignKey('PrimaryResource')

    def __unicode__(self):
        return u'%s' % (self.word)


class Category(models.Model):
    id = models.CharField(max_length=30, unique=True, primary_key=True)
    display_name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return u'%s' % (self.display_name)


class Resource(models.Model):
    id = models.CharField(max_length = 50, unique = True, primary_key=True)
    #want this to be unique, but it can't b/c of the subresources
    name = models.CharField(max_length = 100)
    url = models.URLField() #unique = True)
    desc = models.TextField(blank=True, verbose_name="Description")

    def __unicode__(self):
        return u'%s: %s' % (self.name, self.id) 

class PrimaryResource(Resource):
    shortdesc = models.TextField(blank=True, verbose_name='Short Description')
    longdesc = models.TextField(blank=True, verbose_name='Long Description')
    primary_category = models.ForeignKey(Category, related_name='asPrimaryCategory')
    categories = models.ManyToManyField(Category, related_name='asCategory')
    subresources = models.ManyToManyField(Resource, related_name='asSubResource', verbose_name="Child-Resources")

    def __unicode__(self):
        return u'%s' % self.name
