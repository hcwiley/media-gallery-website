# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Piece.materials'
        db.delete_column('piece_piece', 'materials')

        # Adding field 'Piece.location'
        db.add_column('piece_piece', 'location',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Piece.type'
        db.add_column('piece_piece', 'type',
                      self.gf('django.db.models.fields.CharField')(default='OR', max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Piece.materials'
        db.add_column('piece_piece', 'materials',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Piece.location'
        db.delete_column('piece_piece', 'location')

        # Deleting field 'Piece.type'
        db.delete_column('piece_piece', 'type')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '160', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'OR'", 'max_length': '4'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['piece']