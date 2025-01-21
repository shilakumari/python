import time
import concurrent.futures as cf

def cube(x):
    return x**3
mylist = list(range(10000))

#record start time
start_time = time.time()

with cf.ThreadPoolExecutor() as tpe:
    results=list(tpe.map(cube, mylist))
#print(results)

#record end time
end_time=time.time()
elapsed_times = end_time-start_time
print(f"{elapsed_times} seconds")


#o/p:0.3758871555328369 seconds

