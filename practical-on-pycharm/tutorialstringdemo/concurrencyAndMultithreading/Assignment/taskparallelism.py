import  random
import threading

lock=threading.Lock()

#Task 1
#Random integers between 1 and 100
def generate_numbers():
    l = []
    for _ in range(10):
        lock.acquire()
        num=random.randint(1,100)
        l.append(num)
        lock.release()
    return l

shared_list = generate_numbers()

#Task 2
#Calculate sum of random integers
def calculate_sum():
    sum_shared_list=0
    lock.acquire()
    for i in shared_list:
        sum_shared_list += i
    lock.release()
    return sum_shared_list

t1=threading.Thread(target=generate_numbers)
t2=threading.Thread(target=calculate_sum)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"List with 10 random integers: {generate_numbers()} and their sum: {calculate_sum()}")