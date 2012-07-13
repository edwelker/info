# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resource'
        db.create_table('web_resources_resource', (
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('href', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('web_resources', ['Resource'])

        # Adding model 'Keyword'
        db.create_table('web_resources_keyword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('resource', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web_resources.Resource'])),
        ))
        db.send_create_signal('web_resources', ['Keyword'])

        # Adding model 'SubResource'
        db.create_table('web_resources_subresource', (
            ('resource_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web_resources.Resource'], unique=True, primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='child', to=orm['web_resources.Resource'])),
        ))
        db.send_create_signal('web_resources', ['SubResource'])


    def backwards(self, orm):
        # Deleting model 'Resource'
        db.delete_table('web_resources_resource')

        # Deleting model 'Keyword'
        db.delete_table('web_resources_keyword')

        # Deleting model 'SubResource'
        db.delete_table('web_resources_subresource')


    models = {
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