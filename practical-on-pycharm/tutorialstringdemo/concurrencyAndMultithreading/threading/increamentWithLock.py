import threading
shared_counter=0
lock=threading.Lock()
def increment1():
    global shared_counter
    for i in range(100):
        lock.acquire()
        shared_counter += 1
        lock.release()

def increment2():
    global shared_counter
    for i in range(100):
        lock.acquire()
        shared_counter += 1
        lock.release()

t1=threading.Thread(target=increment1)
t2=threading.Thread(target=increment2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Incremented using lock ",shared_counter)
