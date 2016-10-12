import logging
import os

# get file path 
pwd = os.path.abspath(os.path.dirname(__file__))
dir = os.path.join(pwd, 'Logs')

if not os.path.exists(dir):
    os.mkdir(dir)
    
class Log(object):
    # create a handler
    handler=logging.FileHandler(dir+'/system.log')
    
    #create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.NOTSET)
    
    @classmethod
    def getLogger(self,name='root',level=logging.DEBUG):
        log=logging.getLogger(name)
        log.setLevel(level)
        log.addHandler(self.handler)
        return log
    
if __name__=='__main__':
    x=Log.getLogger('x')
    x.info('X')