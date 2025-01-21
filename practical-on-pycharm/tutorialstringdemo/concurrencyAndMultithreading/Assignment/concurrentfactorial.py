import threading
def calculate_factorial(n):
    if n==0 or n==1:
        return 1
    return n*calculate_factorial(n-1)

for i in range(1, 11):
    t = threading.Thread(target=calculate_factorial, args=(i,))
    t.start()
    print(f"The number {i} and it factorial {calculate_factorial(i)} from thread {t.name}")
    t.join()
