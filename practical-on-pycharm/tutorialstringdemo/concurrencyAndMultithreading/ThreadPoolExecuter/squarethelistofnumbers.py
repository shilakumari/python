import concurrent.futures as cf
def cube(x):
    return x**3

numbers=[1,23,432,23]

#using ThreadPoolExecutor to execute parallel
with cf.ThreadPoolExecutor() as executor:
    results = list(executor.map(cube, numbers))
print(results)#[1, 12167, 80621568, 12167]