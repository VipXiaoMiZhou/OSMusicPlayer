'''
Created on Oct 14, 2016
@author: xxingzh
'''
class Singleton(type):
    __instances = {}
    
    # __call__ makes the class can be use like this:
    # e.g 
    # x=Singleton(args)
    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            self.__instances[self] = super(Singleton,self).__call__(*args,**kwargs)
        return self.__instances[self]

class URLManager(metaclass = Singleton):
    '''URLManager 
        It is a singleton class used to manager all urls.
    '''
    def __init__(self):
        self.url_reposity = set([]) # store all urls
        self.new_url = set([])      # used to store new urls
           
    def addNewUrl(self,urls):
        if len(urls) == 0:
            return
        for url in urls:
            if url in self.url_reposity:
                continue
            else:
                self.new_url.add(url)
          
    def getUrl(self):   
        if len(self.new_url) == 0 :
            return
        url = self.new_url.pop()
        self.url_reposity.add(url)
        return url
     
    def getUrlRepository(self):
        return self.url_reposity
    
if __name__=='__main__':
    x = URLManager()
    y = URLManager()
    urls=['a','b','c','d','e','f']
    x.addNewUrl(urls)
    x.getUrl()
    x.getUrlRepository()
        