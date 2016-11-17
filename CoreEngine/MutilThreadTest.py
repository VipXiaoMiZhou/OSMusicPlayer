import time
import threading
 

product = 0
lock = threading.Condition() 

class Producer(threading.Thread):
    def __init__(self, lock):
        self._lock = lock
        threading.Thread.__init__(self)
 
    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product >= 1000:
                    self._lock.wait()
                else:
                    product += 100
                    print "add 100, product count=" + str(product)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)
 
 
 
 
class Consumer(threading.Thread):
    def __init__(self, lock):
        self._lock = lock
        threading.Thread.__init__(self)
 
    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product <= 100:
                    self._lock.wait()
                else:
                    product -= 3
                    print 'consum 3, count=' + str(product)
                    self._lock.notify()
                self._lock.release()
                time.sleep(1)
 
 
def test():
    for i in range(5):
        p = Producer(lock)
        p.start()
 
    for i in range(5):
        s = Consumer(lock)
        s.start()
 
if __name__ == '__main__':
    test()