from threading import *
from time import sleep


class MyThread1:
    def display_numbers(self):
        i = 0
        print(current_thread().name)
        sleep(1)
        while i <= 10:
            print(i)
            i += 1

obj = MyThread1()
t1 = Thread(target=obj.display_numbers())
t1.start()
print(t1.name)

t2 = Thread(target=obj.display_numbers())
t2.start()
print(t2.name)

t3 = Thread(target=obj.display_numbers())
t3.start()
print(t3.name)

