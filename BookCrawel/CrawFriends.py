'''

'''

import os
import random
import urllib.request
import time
import re
from locale import str

pwd=os.getcwd() #get pwd
cnf_path=os.path.join(os.path.dirname(os.getcwd()),'Config')
log_path=os.path.join(os.path.dirname(os.getcwd()),'Logs')

class Singleton(object):
   # __call__ makes the class can be use like this:
    # e.g
    # x=Singleton(args)
#     def __call__(self, *args, **kwargs):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


'''
URLManager
'''
class URLManager(Singleton):
    '''URLManager
        It is a singleton class used to manager all urls.
    '''
    url_reposity = set([]) # store all urls
    new_url = set([])      # used to store new urls
    
    URLS = [set([]),set([]),set([]),set([])]
    
#     def __init__(self):
#         self.url_reposity = set([]) # store all urls
#         self.new_url = set([])      # used to store new urls
    @staticmethod
    def add_new_url(urls):
        if len(urls) == 0:
            return
        i=0
        for url in urls:
            if url in URLManager.url_reposity:
                continue
            else:
                URLManager.new_url.add(url)
    @staticmethod
    def url_is_empty():
        if len(URLManager.new_url) ==0:
            return True
        else:
            return False
    @staticmethod
    def url_size():
        return len(URLManager.new_url)
    @staticmethod
    def get_url(choice):
        if len(URLManager.new_url) == 0 :
            return
        u = URLManager.new_url.pop()
        
        
        url = URLManager.new_url.pop()
        URLManager.url_reposity.add(url)
        
        for sets in URLManager.URLS:
            sets.add(u)
        
        
        # 0 crawel book info
        if 0 == choice:
            return URLManager.URLS[choice].pop()
        
        # 1 crawel comments
        elif 1 == choice:
            return URLManager.URLS[choice].pop()
        
        elif 2 == choice:
            return URLManager.URLS[choice].pop()
        elif 3 == choice:
            return URLManager.URLS[choice].pop()
        else:
            return "null"
    @staticmethod
    def get_url_repository():
        return URLManager.url_reposity

    

'''ok
'''


class Requester(Singleton):
    @classmethod
    def open_url(self, url):
        head = Disguiser.get_head()
        req = urllib.request.Request(url=url, headers=head)
        html_str = ''
        try:
            # open url and get the reponse
            Response = urllib.request.urlopen(req)
            if Response.status == 200:
                html_str = Response.read().decode('utf-8')
            else:
                # handle other status
                print(Response.header_items())
        except Exception as e:
            print(e)
        Disguiser.delay()
        return html_str


class Disguiser(Singleton):
    '''Disguiser
        Used to disguised http request.
    '''
    user_agent = []

    def __init__(self):
        '''
        Constructor
        '''
        self.head = {
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Accept-Encoding':'gzip, deflate, sdch,utf-8', #here is a problem
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'User-Agent': ''
        }

    def get_agent(self):
        '''get a user-agent from file or a default one.
             read user-agent from user_agent.cnf.when methond was called first time,it will read from file.
        '''
        if len(self.user_agent) == 0:
            try:
                agent = open(os.path.join(cnf_path, 'user_agent.cnf'))
                for line in agent.readlines():
                    # when line is null,return a default one.
                    if line == '':
                        raise Exception
                    line = line[:-1]  # delete '/n' at end of string.
                    self.user_agent.append(line)
            except Exception:
                print('read file err')
                # if err, return a default agent
                return 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
        return random.choice(self.user_agent)

    @staticmethod
    def get_head():
        d = Disguiser()
        d.head['User-Agent'] = d.get_agent()
        return d.head

    @staticmethod
    def delay():
        sec = random.randint(100, 10000)
        time.sleep(sec / 1000)


