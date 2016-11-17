#!/usr/bin/env python
# encoding: utf-8
'''
OSMusicPlayer.CoreEngine.ControlCenter -- shortdesc

OSMusicPlayer.CoreEngine.ControlCenter is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2016 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import time
import random
from CrawFriends import Singleton
from threading import Thread


import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish











def ProducerTest():
    print('hi, I am a producer')
    time.sleep(random.randint(0,10))
    print('hi,I am done')

def Test1():
    print('hahaha, I am Test1')
    time.sleep(10)
    print('Test1 finished')
    
    
def Test2():
    print('hello I am Test2')
    time.sleep(random.randint(0,20))
    print('Test2 finished')

def Test3():
    print('hello I am Test3')
    time.sleep(random.randint(0,10))
    print('Test3 finished')
    
def ConsumerTest():
    print('hello I am a Consumer Application')
    time.sleep(random.randint(10,20))
    print('hello','I\'m consumer and I\'ve done my job')
    pass


def main():
    pass









