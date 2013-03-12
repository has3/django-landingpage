# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LandingPage.call_to_action'
        db.add_column('landingpage_landingpage', 'call_to_action',
                      self.gf('django.db.models.fields.CharField')(default='call to action', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LandingPage.call_to_action'
        db.delete_column('landingpage_landingpage', 'call_to_action')


    models = {
        'landingpage.landingpage': {
            'Meta': {'object_name': 'LandingPage'},
            'call_to_action': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hero_unit': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'point1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'point1'", 'to': "orm['landingpage.Pitch']"}),
            'point2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'point2'", 'to': "orm['landingpage.Pitch']"}),
            'point3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'point3'", 'to': "orm['landingpage.Pitch']"})
        },
        'landingpage.landingpageform': {
            'Meta': {'object_name': 'LandingPageForm'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'landingpage.pitch': {
            'Meta': {'object_name': 'Pitch'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'snippet': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['landingpage']