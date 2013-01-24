# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Piece.name'
        db.delete_column('piece_piece', 'name')


    def backwards(self, orm):
        # Adding field 'Piece.name'
        db.add_column('piece_piece', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=400),
                      keep_default=False)


    models = {
        'piece.myimage': {
            'Meta': {'ordering': "['image']", 'object_name': 'MyImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'piece.piece': {
            'Meta': {'object_name': 'Piece'},
            'default_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'piece_piece_default_image'", 'null': 'True', 'to': "orm['piece.MyImage']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '160', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'GREEN'", 'max_length': '7'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'ART'", 'max_length': '6'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['piece']