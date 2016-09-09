from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Submission(models.Model):
    """
    Represents a submission of genomics to be tested
    """
    
    label = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "%s " % (self.label)
    