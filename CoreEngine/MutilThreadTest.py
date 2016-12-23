import time
import threading


product = 0
lock = threading.Condition() 

class Producer(threading.Thread):
    def __init__(self, lock):
        lock = lock
        threading.Thread.__init__(self)
 
    def run(self):
        global product
        
        index = 0
        while True:
            if index > 10 :
                break
            
            
            
            if lock.acquire():
#                 if product >= 1000:
                if Spider.pub_url_manager.url_size() > 100:
                    lock.wait()
                    pass
                else:
                    Spider.crawl_url('随笔', index)
                    index = index + 1
                    product += 100
                    print ("add 100, product count=" + str(product))
                    lock.notify()
                lock.release()
                time.sleep(1)
            
            
 
 
 
 
#  
class Consumer(threading.Thread):
    def __init__(self, lock):
        lock = lock
        threading.Thread.__init__(self)
  
    def run(self):
        global product
        while True:
            if lock.acquire():
#                 if product <= 100:
                if Spider.pub_url_manager.url_size() < 20:
                    lock.wait()
                else:
                    product -= 3
                    print ('consum 3, count=' + str(product))
                    print('url',Spider.pub_url_manager.get_url(0))
                    lock.notify()
                lock.release()
                time.sleep(1)
 


# class Consumer(threading.Thread):
#     def __init__(self, lock):
#         lock = lock
#         threading.Thread.__init__(self)
#  
#     def run(self):
#         global product
#         index = 0;
#         while True:
#             
#             if index > 10:
#                 break
#             if lock.acquire():
#                 if Spider.pub_url_manager.url_size() < 100:
#                     Spider.crawl_url('随笔', index)
#                     print('size',Spider.pub_url_manager.url_size())
#                     lock.wait()
#                 else:
#                     product -= 3
#                     print ('consum 3, count=' + str(product))
#                     lock.notify()
#                 lock.release()
#                 time.sleep(1)
#             index = index + 1
 
def test():
    pass
#     for i in range(5):
#         p = Producer(lock)
#         p.start()
#  
#     for i in range(5):
#         s = Consumer(lock)
#         s.start()
#  
if __name__ == '__main__':
    p = Producer(lock)
    c = Consumer(lock)
    
    p.start()
    c.start()
#     test()