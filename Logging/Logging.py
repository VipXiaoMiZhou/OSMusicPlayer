'''
Created on Oct 10, 2016

@author: xxingzh
'''
import logging
import logging.config
import os
import ConfigParser


pwd=os.path.abspath(os.path.dirname(__file__))
dir=os.path.join(pwd,'Logs')
logging.config.fileConfig(pwd + '/logging.cnf')
class Logger(object):
    @classmethod
    def getLogger(self,log='root'):
        try:
            l=logging.getLogger(log)
        except Exception:
            l=logging.getLogger()
        return l

if __name__=='__main__':
    log=Logger.getLogger('normal')
    log.debug('this is a debug message')
    log.error('this is a debug message')