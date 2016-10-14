import logging
import os

# get file path 
pwd = os.path.abspath(os.path.dirname(__file__))
dir = os.path.join(pwd, 'Logs')

if not os.path.exists(dir):
    os.mkdir(dir)

class Singleton(type):
    __instances = {}
    
    # __call__ makes the class can be use like this:
    # e.g 
    # x=Singleton(args)
    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            self.__instances[self] = super(Singleton,self).__call__(*args,**kwargs)
        return self.__instances[self]

class Log(metaclass = Singleton):
    # create a handler
    handler=logging.FileHandler(dir+'/system.log')
    
    #create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  %(message)s')
    handler.setFormatter(formatter)
    handler.setLevel(logging.NOTSET)
    
    @classmethod
    def getLogger(self,name='root',level=logging.DEBUG):
        log=logging.getLogger(name)
        log.setLevel(level)
        log.addHandler(self.handler)
        return log
    
    
if __name__=='__main__':
    # useage
    x=Log.getLogger('X')
    x.info('X')