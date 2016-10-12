'''
Created on Oct 10, 2016
@author: xxingzh.
@description : UIA controller.
@date: 10/10/2016 4:03 PM.
@group: XiaoMiZhou Team.
'''
from UI import UI
from Logging.Logging import Logger
class Controller(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        ui = UI()     # import UIA module
        self.params = params 
    def about(self):
        ui.about();
     
    def list(self, list):
        ui.list(list)
    
    def help(self,hp):
        ui.help(hp)
    
        
if __name__ == "__main__":
    ui = UI()
    ui.about()
    d = {'x':'fdfsdfsf', 'y':'asdasd', 'z':'asddd'}
    ui.help(d)
    x = Controller('dfd')
    print x.params