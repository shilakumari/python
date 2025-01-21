import threading

shared_counter=0
lock=threading.Lock()
def increment_counter():
    global shared_counter
    shared_counter += 1

t1=threading.Thread(target=increment_counter)
t2=threading.Thread(target=increment_counter)
t1.start()
t2.start()
t1.join()
t2.join()
if t1.name:
    for _ in range(1,1000):
        lock.acquire()
        increment_counter()
        lock.release()
if t2.name:
    for _ in range(1,1000):
        lock.acquire()
        increment_counter()
        lock.release()

print(shared_counter)