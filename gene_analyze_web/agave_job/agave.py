'''
Created on Sep 8, 2016

@author: walling
'''
from agavepy.agave import Agave


def connect():
    my_agave = Agave(api_server='https://agave.iplantc.org', username='myusername', password='mypassword')
    
def push_file():