import concurrent.futures as cf

myList=[1,6,8,9]

def cube(x):
    return x**3

with cf.ThreadPoolExecutor() as e:
    results=list(e.map(cube,myList))
print(results)