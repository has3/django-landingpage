from django.db import models

# Create your models here.
# type (not necessarily primitive), object
class LandingPageForm(models.Model):
    # descriptor (advanced class feature)
    # differs from getter/setter
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name + "'s response"

class LandingPage(models.Model):
    hero_unit = models.ImageField(upload_to="images/hero")
    call_to_action = models.CharField(max_length=255)
    point1 = models.ForeignKey('Pitch', related_name='point1')
    point2 = models.ForeignKey('Pitch', related_name='point2')
    point3 = models.ForeignKey('Pitch', related_name='point3')

    def __unicode__(self):
        return self.call_to_action

class Pitch(models.Model):
    image = models.ImageField(upload_to="images/pitch")
    snippet = models.CharField(max_length=255)
    snippet_heading = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.snippet



    