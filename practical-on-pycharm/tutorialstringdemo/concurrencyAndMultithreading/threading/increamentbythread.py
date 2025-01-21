import threading
shared_counter=0
def increment1():
    global shared_counter
    for i in range(100):
        shared_counter += 1

def increment2():
    global shared_counter
    for i in range(100):
        shared_counter += 1

t1=threading.Thread(target=increment1)
t2=threading.Thread(target=increment2)
t1.start()
t2.start()
t1.join()
t2.join()
print(shared_counter)
