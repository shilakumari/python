import threading
import time
def cal_square(num):
    print("Calculate the square of the given number")
    for n in num:
        time.sleep(0.3)# at iteration, it waits for 0.3 times
        print("Square is: ",n*n)
arr=[4,5,6,7,2]

t1=time.time()#get total time to execute the function

thread1=threading.Thread(target=cal_square,args=(arr,))
thread1.start()

#cal_square(arr)
print("Total time taken by threads is: ", time.time()-t1)
thread1.join()#join() insures that after completion of "thread1" next line should execute

print("Hi")
