'''
Created on Dec 7, 2016

@author: zhangxing
'''

import threading  
from CrawFriends import URLManager
from Spider import Spider
import ResultHandler
condition = threading.Condition()  
products = 0  
 
urls = URLManager()

class Producer(threading.Thread):  
    def __init__(self,keyoword):
        self.keyword = keyoword  
        threading.Thread.__init__(self)  
 
    def run(self):  
        global condition, products, urls
        while True:  
            if condition.acquire():
                if urls.url_size() <= 20:
                    urls.add_new_url(Spider.crawl_url(self.keyword, products))
                    products +=1;
                    print ("Producer(%s):deliver one, now products:%s" %(self.name, urls.url_size()))
                    condition.notify()
                    pass
                else:
                    condition.wait()   
                # stop     
                if products >= 100:
                    break;  
                condition.release()   

class Consumer(threading.Thread):  
    def __init__(self):  
        threading.Thread.__init__(self)  
 
    def run(self):  
        global condition, products, urls  
        while True:  
            if condition.acquire():  
                
                if urls.url_size() > 20:
                    url = urls.get_url(0)
                    print ("Consumer(%s):consume one, now products:%s" %(self.name,url))
                    condition.notify()
                else:
                    condition.wait()
                    print ("Consumer(%s):consume one, now products:%s" %(self.name, products))        
                condition.release()   
 
 
if __name__ == "__main__": 
          
    p = Producer('历史')  
    p.start()  
 
    p1 = Producer('随笔')
    p1.start()
    
    p3 = Producer('小说')
    p3.start()
    
    for c in range(0, 10):  
        c = Consumer()  
        c.start()
