class MetaSingleton(type):
	instance = None
    	def __call__(self, *args, **kw):
        	if self.instance is None:
           	self.instance = super(MetaSingleton, self).__call__(*args, **kw)
	return self.instance

class Foo(object):
	__metaclass__ = MetaSingleton

a = Foo()
b = Foo()
print(id(a))
print(id(b))
