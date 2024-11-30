import threading
from threading import Thread

print("Current Thread that is running: ",threading.current_thread().name)

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Some other thread")

