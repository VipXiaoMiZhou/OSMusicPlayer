class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello,how are you ',self.name,'?')
p=Person('xxingzh')
p.say_hi()
