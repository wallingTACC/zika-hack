'''
Created on Sep 8, 2016

@author: walling
'''
from agavepy.agave import Agave
import agave_config as ac
import tempfile

def connect():
    my_agave = Agave(api_server=ac.API_SERVER, client_name=ac.CLIENT_NAME,
                     token=ac.ACCESS_TOKEN, refresh_token=ac.REFRESH_TOKEN,
                     api_key=ac.AGAVE_API_KEY, api_secret=ac.API_SECRET,)
    return my_agave

def run_job(submission="test-submit.tar.gz"):
    
    agave = connect()
    
    job = {
      "name": submission,
      "appId": ac.APP_ID,
      "inputs": {
        "temp": ["agave://" + ac.DATA_SYSTEM + "/" + ac.DATA_DIR + "/" + submission]
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
    return my_job

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

def list_files(path):
    agave=connect()
    
    result = agave.files.list(systemId=ac.DATA_SYSTEM, filePath=ac.DATA_DIR)     
    return result

def new_submission(submission):
    return None

if __name__ == '__main__':
    """
    Used for simple debugging
    """
    #django.setup()
    a = 'a'
    