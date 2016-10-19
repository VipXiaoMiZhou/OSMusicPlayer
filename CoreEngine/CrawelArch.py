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
import re
from locale import str
from reportlab.graphics.charts.utils import seconds2str
from bs4.tests.test_docs import __metaclass__

config = configparser.ConfigParser()
__all__ = []
__version__ = '0.0.1'
__date__ = '2016-10-14'
__updated__ = '2016-10-14'

'''
Created on Oct 14, 2016
@author: xxingzh
'''
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
class URLManager():
    '''URLManager 
        It is a singleton class used to manager all urls.
    '''
    url_reposity = set([]) # store all urls
    new_url = set([])      # used to store new urls
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
    def is_empty():
        if len(URLManager.new_url) ==0:
            return True
        else:
            return False
    @staticmethod
    def size():
        return len(URLManager.new_url)
    @staticmethod     
    def get_url():   
        if len(URLManager.new_url) == 0 :
            return
        url = URLManager.new_url.pop()
        URLManager.url_reposity.add(url)
        return url
    @staticmethod
    def get_url_repository():
        return URLManager.url_reposity
    
  
'''ok
'''
class Requester(Singleton):
    @classmethod
    def open_url(self,url):   
        head=Disguiser.get_head()
        req = urllib.request.Request(url=url,headers=head)
        html_str=''
        try:
            # open url and get the reponse
            Response = urllib.request.urlopen(req)
            if Response.status==200:
                html_str=Response.read().decode('utf-8')
            else:
                # handle other status
                print(Response.header_items())
        except Exception as e:
            print(e)
        Disguiser.delay()
        return html_str
 

'''ok
'''    
class Disguiser(Singleton):
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
    def get_head():
        d = Disguiser()
        d.head['User-Agent'] = random.choice(d.user_agent)
        return d.head

    @staticmethod
    def delay():
        sec=random.randint(100,10000)
        time.sleep(sec/1000)
        

class HtmlParser():
    '''HtmlParser
        Used to parse html.
    '''        
    @staticmethod
    def parse(html_str):
        print(html_str)
        return 'result'

  
class ResultHander(object):
    __metaclass__=Singleton
    def dohandle(self,result):
        pass
    pass


class url_parse(HtmlParser):
    
    pass

class Spide():
    parser=HtmlParser()
    pub_url_manager=URLManager()
    result_handler=ResultHander()
    x=Requester()
    # https://book.douban.com/tag/%E9%9A%8F%E7%AC%94
    @staticmethod
    def do_crawel(keyword,start,offset):
        
        if start==0 : start=1
        if (start > offset) or (start< 0) or (offset< 0):
            print('Input  Illegal, Please Check Input and Run Again!')
            return
        ur=URLManager()
        subject = 'https://book.douban.com/tag/'
        data={
              'tag':urllib.parse.quote(keyword),
              'start':0,
              'type':'T'
              }
        while True: 
            data['start']=(start-1)*20
            url=subject+data['tag']+'?start='+str(data['start'])+'&type='+data['type']
            html_str=Requester.open_url(url)
            if html_str == '':
                print('end')
                return
#             urls=HtmlParser.get_url_from_html(html_str,r"https://book.douban.com/subject/\d+")
            urls=re.findall(r"https://book.douban.com/subject/\d+", html_str)
            ur.add_new_url(urls)
            print(len(urls),urls)
            print(url)
            print(ur.size())
#             while URLManager.is_empty():
#                 html=Spide.request.open_url(url)
#                 result=HtmlParser.parse(html)
#                 ResultHander.dohandle(result) 
            start=start+1
            if ((start-1)*20) >((offset-1)*20):
                break
    def craw_books(self,keyword,start,offset):
        #https://book.douban.com/subject/20427187/comments/hot?p=1
        pass
    
    @staticmethod
    def craw_comments(keyword,start,offset):
        if keyword=='':return
        while True:
            url='https://book.douban.com/subject/'+str(keyword)+'/comments/hot?p='+str(start)
            print(url)
            html_str=Requester.open_url(url)
            print(html_str)
            if html_str=='':
                print('end')
                return
#             ResultHander.dohandle(HtmlParser.parse(html_str))
            start=start+1
            if start > offset:
                break
    @staticmethod
    def craw_annotations(keyword,start,offset):
        #https://book.douban.com/subject/20427187/annotation?sort=rank&start=0
        if keyword=='' or start>offset or start<0:
            print('Input  Illegal, Please Check Input and Run Again!')
            return
        data={
              'action':'https://book.douban.com/subject/',
              'keyword':keyword,
              'tag':'annotation',
              'sort':'rank',
              'start':start
              }
        url_manager=URLManager()
        while True:
            data['start']=(start-1)*10
            url=data['action']+data['keyword']+'/'+data['tag']+'?'+'sort='+data['sort']+'&'+'start='+str(data['start'])
            print(url)
            html_str=Requester.open_url(url)
            #https://book.douban.com/annotation/23575193/
            urls=re.findall(r"https://book.douban.com/annotation/\d+", html_str)
            url_manager.add_new_url(urls)
            print(len(urls),urls)
#             while url_manager.is_empty():
#                 url=url_manager.get_url()
#                 html=Requester.open_url(url)
#                 #ResultHander.dohandle(HtmlParser.parse(html))
#             pass
            print(url_manager.size())
            start=start+1
            if ((start-1)*10)>((offset-1)*10):
                break
        pass
    def craw_reviews(self,keyword,start,offset):
        pass
    
    
if __name__=='__main__':
    
#     Spide.do_crawel('历史',2,3)
#     
#     Spide.craw_comments(20427187,1 ,2)
    Spide.craw_annotations(str(20427187), 1, 2)
    
    