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


class Resource(models.Model):
    id = models.CharField(max_length = 50, unique = True, primary_key=True)
    #want this to be unique, but it can't b/c of the subresources
    name = models.CharField(max_length = 100)
    url = models.URLField() #unique = True)
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.title)


class PrimaryResource(Resource):
    shortdesc = models.TextField(blank=True)
    longdesc = models.TextField(blank=True)
    primary_category = models.ForeignKey(Category)
    categories = models.ManyToManyField(Category)
