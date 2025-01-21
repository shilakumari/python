import time
import threading

def task(name,duration):
    print(f"Task {name} starting...")
    time.sleep(duration)
    print(f"Task {name} completed!- Duration:{duration}")

tasks=[("Task1",3),("Task2",3),("Task3",3)]

#Sequential execution
start_time=time.time()
print("Starting sequential execution...")
for name, duration in tasks:
    task(name, duration)
end_time=time.time()

sequential_time=end_time-start_time
print(f"Sequential execution completed in {sequential_time:.2f} seconds\n")

#Threading execution
start_time=time.time()
print("Starting thread execution...")
threads=[]
for t, d in tasks:
    th= threading.Thread(target=task, args=(name,duration))
    threads.append(th)
    th.start()

#wait for all threads to complete
for t in threads:
    t.join()

end_time=time.time()
threaded_time=time.time()
print(f"Threaded execution completed in {threaded_time:.2f} seconds\n")
print(f"Time saved: {sequential_time-threaded_time:.2f} seconds")
