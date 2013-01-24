# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Piece.time'
        db.add_column('piece_piece', 'time',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Piece.date'
        db.add_column('piece_piece', 'date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Piece.time'
        db.delete_column('piece_piece', 'time')

        # Deleting field 'Piece.date'
        db.delete_column('piece_piece', 'date')


    models = {
        'piece.myimage': {
            'Meta': {'ordering': "['image']", 'object_name': 'MyImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'piece.piece': {
            'Meta': {'object_name': 'Piece'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'default_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'piece_piece_default_image'", 'null': 'True', 'to': "orm['piece.MyImage']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '160', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'GREEN'", 'max_length': '7'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'ART'", 'max_length': '6'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['piece']