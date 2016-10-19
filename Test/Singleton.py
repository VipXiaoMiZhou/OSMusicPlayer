'''
Created on Oct 18, 2016

@author: zhangxing
'''

class Singleton(object):
    _inst = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args)
        return cls._inst[cls]


class MyClass(Singleton):
    __metaclass__ = Singleton


if __name__ == '__main__':
    a=MyClass()
    b=MyClass()
    
    print(a==b)