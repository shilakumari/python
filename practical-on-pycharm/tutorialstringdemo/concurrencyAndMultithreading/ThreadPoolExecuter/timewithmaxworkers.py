import time
import concurrent.futures as cf

def cube(x):
    return x**3
mylist = list(range(10000))

#record start time
start_time = time.time()

with cf.ThreadPoolExecutor(max_workers=2) as tpe:
    cubes=tpe.submit(cube,mylist)
#print(cubes)

#record end time
end_time=time.time()
print(end_time-start_time)#o/p:0.01042485237121582
