# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pitch'
        db.create_table('landingpage_pitch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('snippet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('landingpage', ['Pitch'])

        # Adding model 'LandingPage'
        db.create_table('landingpage_landingpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hero_unit', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('point1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='point1', to=orm['landingpage.Pitch'])),
            ('point2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='point2', to=orm['landingpage.Pitch'])),
            ('point3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='point3', to=orm['landingpage.Pitch'])),
        ))
        db.send_create_signal('landingpage', ['LandingPage'])


    def backwards(self, orm):
        # Deleting model 'Pitch'
        db.delete_table('landingpage_pitch')

        # Deleting model 'LandingPage'
        db.delete_table('landingpage_landingpage')


    models = {
        'landingpage.landingpage': {
            'Meta': {'object_name': 'LandingPage'},
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