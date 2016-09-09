'''
Created on Sep 7, 2016

@author: walling
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # /agave_job/
    
    # Submission Form
    url(r'^submissionForm/$', views.submission_form, name='submission_form'), #/submissionForm/
    url(r'^submissionForm/(?P<submission_id>\d+)/$', views.submission_form, name='submission_form'), #/submissionForm/SubmissionID/

    # Detail View
    url(r'^submission(?P<submission_id>[0-9]+)/$', views.submission_details, name='submission_details')
]