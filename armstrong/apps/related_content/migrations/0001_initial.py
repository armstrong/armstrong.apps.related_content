# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RelatedType'
        db.create_table('related_content_relatedtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('related_content', ['RelatedType'])

        # Adding model 'RelatedContent'
        db.create_table('related_content_relatedcontent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('related_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['related_content.RelatedType'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('source_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from', to=orm['contenttypes.ContentType'])),
            ('source_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('destination_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to', to=orm['contenttypes.ContentType'])),
            ('destination_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('related_content', ['RelatedContent'])


    def backwards(self, orm):
        
        # Deleting model 'RelatedType'
        db.delete_table('related_content_relatedtype')

        # Deleting model 'RelatedContent'
        db.delete_table('related_content_relatedcontent')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'related_content.relatedcontent': {
            'Meta': {'ordering': "['order']", 'object_name': 'RelatedContent'},
            'destination_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'destination_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'related_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['related_content.RelatedType']"}),
            'source_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'source_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'to': "orm['contenttypes.ContentType']"})
        },
        'related_content.relatedtype': {
            'Meta': {'object_name': 'RelatedType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['related_content']
