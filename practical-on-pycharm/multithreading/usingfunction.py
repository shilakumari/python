import threading
from threading import *

def displayMyNumbers():
    i = 0
    while i <= 10:
        print(i)
        i += 1

print(threading.current_thread().name)#Main thread

# creating thread using function displayMyNumbers
t = Thread(target=displayMyNumbers())
t.start()
print(t.name)#Thread-1