class Robot:
    __author__ = "carvin"
    __date__ = "now"
    __location__ = "Shanghai"
    # a class varible
    population = 0
    def __init__(self,name):
        self.name = name
        print self.name
        Robot.population += 1
    def die(self):
        print self.name
        Robot.population -= 1
        if Robot.population == 0 :
            print self.name
        else :
            print "Greeting,my master call me."
    def say_hi(self):
        print self.name



    @classmethod
    def nice(word):
        print word
a = Robot("DD-2")
a.say_hi()
b = Robot("CC-1")
b.say_hi()









