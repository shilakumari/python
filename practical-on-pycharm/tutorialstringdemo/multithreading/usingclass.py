from threading import *
class MyThread:
    def display_numbers(self):
        i = 0
        while i <= 10:
            print(i)
            i += 1

obj = MyThread()
t = Thread(target=obj.display_numbers())
t.start()
print(t.name)


