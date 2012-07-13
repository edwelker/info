# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('web_resources_category', (
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30, primary_key=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('web_resources', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('web_resources_category')


    models = {
        'web_resources.category': {
            'Meta': {'object_name': 'Category'},
            'display_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'})
        },
        'web_resources.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['web_resources.Resource']"}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web_resources.resource': {
            'Meta': {'object_name': 'Resource'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'href': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'web_resources.subresource': {
            'Meta': {'object_name': 'SubResource', '_ormbases': ['web_resources.Resource']},
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child'", 'to': "orm['web_resources.Resource']"}),
            'resource_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['web_resources.Resource']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['web_resources']