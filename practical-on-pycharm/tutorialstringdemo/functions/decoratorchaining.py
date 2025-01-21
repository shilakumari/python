#Decorator for half
def half(fun):
    def inner():
        n=fun()
        return n/2
    return inner

#Decorator for square
def square(fun):
    def inner():
        n=fun()
        return n*n
    return inner

@square
@half
def num():
    return 10

print(num())