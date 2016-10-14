'''
Created on Oct 10, 2016
@author: xxingzh.
@description : UIA controller.
@date: 10/10/2016 4:03 PM.
@group: XiaoMiZhou Team.
'''
from UI import UI
from Logging.Logger import Log
import ConfigParser
from distutils.command.config import config

class Controller(object):
    '''
    classdocs
    '''
    PLAY='play'
    STOP='stop'
    ABOUT='about'
    LIST='list'
    PAUSE='pause'
    HELP='help'
    
    
    logger=Log.getLogger('UIController')  
    ui=UI()

    def about(self):
        self.ui.about(); 
    def list(self, list):
        def list(list):
            '''parse list to a prop list we want
            '''
            pass
        self.ui.list(list)
    
    def help(self):
        def read_helpfile():
            self.logger.info('ready to read help.ini')
            config=ConfigParser.ConfigParser()
            try:
                self.logger.info('reading help.ini')
                config.readfp(open('/home/xxingzh/workspace/vbox/OSMusicPlayer/Config/help.ini'))
                section=config.sections()
                hp= {}
                for s in section:
                    for op in config.items(s):
                        hp[op[0]]=op[1]   
            except Exception:
                self.logger.error('reading help.ini error')
            return hp   
        self.ui.help(read_helpfile())
        
    def play(self,playinfo):
        if playinfo=='':
            return
        def parse(data):
            '''convert & choice date what play function wanted
            '''
            pass
        self.ui.play(playinfo)
    def stop(self):
        pass
    @staticmethod
    def dispatch(ope,data):
        c=Controller()
        if ope=="play":
            c.play(data)
        elif ope=="help":
            c.help()
        elif ope=="stop":
            pass
        elif ope=="about":
            c.about()
        elif ope=="list":
            c.list(data)
        elif ope=="pause":
            pass
        else:
            pass
        pass
    
        
if __name__ == "__main__":
    c = {'singer':'Kobe','song':'You are a gay','year':'2012.03.21','amblu':'tomorrrow'}
    l ='[{"name": "QQ music","list":[{"singer": "John","song": "Doe"},{"singer": "Anna","song": "Smith"},{"singer": "Peter","song": "Jones"}]}]'
    Controller.dispatch(Controller.PLAY, c)
    Controller.dispatch(Controller.HELP, c)
    Controller.dispatch(Controller.ABOUT, c)
    Controller.dispatch(Controller.LIST,l)