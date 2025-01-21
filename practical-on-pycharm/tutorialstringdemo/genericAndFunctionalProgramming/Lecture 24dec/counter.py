import threading
shared_counter=0

#Function to increment the counter
def increment_counter():
    global shared_counter
    for _ in range(1000):
        shared_counter += 1

#Creating threads
threads=[]
for _ in range(2):
    th=threading.Thread(target=increment_counter)
    threads.append(th)
    th.start()

#Waiting for all threads to complete
for t in threads:
    t.join()

print(f"Final counter value: ",shared_counter)#Final counter value:  2000

