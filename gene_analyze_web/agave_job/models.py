from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Submission(models.Model):
    """
    Represents a submission of genomics to be tested
    """
    
    label = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    lng = models.DecimalField(max_digits=8, decimal_places=3)
    datetime = models.DateTimeField()
    
    result = models.NullBooleanField(null=True)
    
    submission_file = models.FileField(null=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.label, self.datetime)
    