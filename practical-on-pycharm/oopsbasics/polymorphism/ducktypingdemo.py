#Duck tying
class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hello")

def callTalk(obj):
    obj.talk()

d1=Duck()
callTalk(d1)

h1=Human()
callTalk(h1)

