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
from bs4 import BeautifulSoup 

config = configparser.ConfigParser()
__all__ = []
__version__ = '0.0.1'
__date__ = '2016-10-14'
__updated__ = '2016-10-14'

'''
Created on Oct 14, 2016
@author: xxingzh
'''
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
   
class Disguiser(Singleton):
    '''Disguiser
        Used to disguised http request.
    '''
    user_agent=[]
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
        
    def get_agent(self):
        '''get a user-agent from file or a default one.
             read user-agent from user_agent.cnf.when methond was called first time,it will read from file.
        '''
        if len(self.user_agent)==0:
            try:
                agent=open(os.path.join(cnf_path,'user_agent.cnf'))
                for line in agent.readlines():
                    # when line is null,return a default one.
                    if line=='':
                        raise Exception
                    line=line[:-1]  #delete '/n' at end of string.
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

class Spider():
    parser=HtmlParser()  
    pub_url_manager=URLManager()    
    result_handler=ResultHander()
    x=Requester()
    # https://book.douban.com/tag/%E9%9A%8F%E7%AC%94
    @staticmethod
    def do_crawel(keyword,start,offset):
        pass
     
        
    def crawl_url(self,keyword,start,offset):
        #https://book.douban.com/subject/20427187/comments/hot?p=1
        if start==0 : start=1
        if (start > offset) or (start< 0) or (offset< 0):
            print('Input  Illegal, Please Check Input and Run Again!')
            return
        data={
              'action':'https://book.douban.com/tag/',
              'tag':urllib.parse.quote(keyword),
              'start':0,
              'type':'T'
              }
        while True: 
            data['start']=(start-1)*20
            url=data['action']+data['tag']+'?start='+str(data['start'])+'&type='+data['type']
            html_str=Requester.open_url(url)
            urls=re.findall(r"https://book.douban.com/subject/\d+", html_str)
            self.pub_url_manager.add_new_url(urls)
            start=start+1
            if ((start-1)*20) >((offset-1)*20):
                break
    
    @classmethod
    def crawl_comments(self,keyword,start,offset):
        if keyword=='':return
        keyword=str(keyword)
        result={'bookid':keyword,'comment-info':[]}
        while True: 
            url='https://book.douban.com/subject/'+keyword+'/comments/hot?p='+str(start)
            html_str=Requester.open_url(url)
            soup = BeautifulSoup(html_str,'lxml')
            for item in soup.find_all('li',class_="comment-item"):
                info={'commentator':'',
                  'avatar':'',
                  'commentator_homepage':'',
                  'comment_content':'',
                  'comment_date':'',
                  'comment_vote':'',
                  'star':''
                }
                info['commentator']=item.a['title']            # title
                info['commentator_homepage']=item.a['href']    # homepage
                info['avatar']=item.img['src']                 # avatar image
                info['comment_content']=item.p.text            # comment_content
        
                # comment date
                comment_data=item.find_all(text=re.compile(r'\d{4}-\d{2}-\d{2}'))
                if len(comment_data)>0:
                    info['comment_date']=comment_data[0].string
                    # vote_count
                vote_count=item.find_all('span',class_='vote-count')    
                if len(vote_count)>0:
                    info['comment_vote']=vote_count[0].text
                else:
                    info['comment_vote']=0
        
                # start  
                # <span class="user-stars allstar50 rating" title="力荐"></span>
                star=item.find_all('span',class_=re.compile(r'(?<=allstar)\d+'))
                if(len(star))>0:
                    z=star[0].attrs['class']  # ['user-stars','allstar50','rating']
                    if len(z)>1:
                        point=z[1]
                        s=re.findall(r'\d+',point)   #['50']
                        if len(s)>=0:
                            info['star']=s[0]   #50
#                             print(s[0])
                        else:
                            info['star']=0
#                 print(info)
#                 resultx.append(info)
                result['comment-info'].append(info)
#             print(resultx) 
            start=start+1
            if start > offset:
                print(result)
                break
    @staticmethod
    def crawl_annotations(keyword,start,offset):
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
    
    
    def crawl_reviews(self,keyword,start,offset):
        pass
    
    
if __name__=='__main__':
    
#     Spide.do_crawel('历史',2,3)
#     
    Spider.crawl_comments(20427187,1,5) 