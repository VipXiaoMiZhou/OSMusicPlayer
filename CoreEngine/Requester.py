#!/usr/local/bin/python2.7
# encoding: utf-8
'''
CoreEngine.Requester -- shortdesc

CoreEngine.Requester is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2016 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''
from CoreEngine.Disguiser import Disguiser
import urllib.request as q
import urllib
import datetime
import time
__all__ = []
__version__ = 0.1
__date__ = '2016-10-14'
__updated__ = '2016-10-14'


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
if __name__=='__main__':
    x=Requester()
    print (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
      
    x.openUrl('http://www.jianshu.com/p/de4af954fcbe')
    print('Ok')
    print (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))