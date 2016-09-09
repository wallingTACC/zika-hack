'''
Created on Sep 8, 2016

@author: walling
'''
from agavepy.agave import Agave
import agave_config as ac
import tempfile

from .models import Submission

def connect():
    my_agave = Agave(api_server=ac.API_SERVER, username=ac.USERNAME, password=ac.PW, client_name=ac.CLIENT_NAME)
    return my_agave

def push_file(submission):
    
    agave=connect()
    temp = tempfile.mktemp()

    with open(temp, 'w') as f:
        f.write('Hello world!')
        
    response = agave.files.importData(
        systemId=ac.DATA_SYSTEM,
        filePath=ac.DATA_DIR,
        fileName='hello.txt',
        fileToUpload=open(temp))
    
    return response
    
def run_job(submission):
    agave = connect()
    
    job = {
      "name": submission.label,
      "appId": ac.APP_ID,
      "inputs": {
        "temp": ["agave://my.test.system//{HOME_DIR}/hello.txt".format(HOME_DIR="HOME_DIR")]
      },
      "archive": True,
      "notifications": [
        {
          "url": "http://requestb.in/p9fm7ap9?job_id=${JOB_ID}&status=${JOB_STATUS}",
          "event": "*",
          "persistent": True
        }
      ]
    }
    
    my_job = agave.jobs.submit(body=job)
    my_job

