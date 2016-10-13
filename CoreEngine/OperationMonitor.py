'''
Created on Oct 12, 2016

@author: xxingzh
'''
import tty, sys, time
import threading

# tty.setraw(sys.stdin.fileno())

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while 1:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name
 
print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name


# class Operator(object):
#     '''
#     classdocs
#     '''
#     operator=''
#     def getOperator(self):
#         while 1:
#             # read input
#             self.operator = sys.stdin.read(1)
#             time.sleep(1)
#      
#     def test(self):
#         print 'sss'
#         n=50
#         while 1:
#             print n+1
#             if n>50:
#                 break
#             time.sleep(1)
# if __name__=='__main__':
#     print 'xxxxxx'
#     x = Operator()
#     t = threading.Thread(target=x.getOperator())
#     
#     
#     t1 = threading.Thread(target=x.test())
#     
#     t.start()
#     t.join()
#     
#     t1.start()
#     t1.join()
#     
#     print 'ssss'
#                 
#         