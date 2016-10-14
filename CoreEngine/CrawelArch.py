#!/usr/bin/env python
# encoding: utf-8
'''
CoreEngine.CrawelArch -- shortdesc

CoreEngine.CrawelArch is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2016 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import configparser
import random
import urllib.request
import datetime
import time

config = configparser.ConfigParser()
__all__ = []
__version__ = '0.0.1'
__date__ = '2016-10-14'
__updated__ = '2016-10-14'

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

'''

'''
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
  
  
class Requester(object):
    def openUrl(self,url):   
        head=Disguiser.getHead()
        req = urllib.request.Request(url=url,headers=head)
        with urllib.request.urlopen(req) as r:
            print(type(r.status))
            if r.status==200:
                pass
            else:
                return
            print(req.header_items())
            print (r.read().decode('utf-8'))



class Disguiser(object):
    '''Disguiser
        Used to disguised http request.
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.head={
                   'Connection':'keep-alive',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   #'Accept-Encoding':'gzip, deflate, sdch,utf-8', #here is a problem
                   'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                   'User-Agent':''
                   }
        self.user_agent=[
                         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                         'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
                         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                         'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
                         'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
                         'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'
                         ]
    @staticmethod
    def getHead():
        x = Disguiser()
        def readIniFile():
            pass
        x.head['User-Agent'] = random.choice(x.user_agent)
        return x.head
    

   
if __name__=='__main__':
    
    x=Requester()
    print (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
      
    x.openUrl('http://www.jianshu.com/p/de4af954fcbe')
    print('Ok')
    print (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    
    