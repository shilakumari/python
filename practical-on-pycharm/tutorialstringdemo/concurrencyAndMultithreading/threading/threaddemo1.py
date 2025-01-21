import threading
def greet():
	print("Hello from a thread!")
t=threading.Thread(target=greet)
t.start()
t.join()
#Hello from a thread!
