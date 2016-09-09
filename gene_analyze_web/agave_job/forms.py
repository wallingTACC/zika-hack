'''
Created on Sep 8, 2016

@author: walling
'''
from django import forms

class SubmissionForm(forms.Form):
    label = forms.CharField(label='Submission Label', max_length=100)