'''
Created on Oct 10, 2016

@author: xxingzh
'''
import logging
import logging.config
class Log(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.log = logging.basicConfig(filename='example.log',level=logging.INFO)
