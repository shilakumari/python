#Double the given number
def decorfun(fun):
    def inner():
        result=fun()
        return result*2
    return inner

def num():
    return 5
d=decorfun(num)
print(d())

#using @, to apply decorator to a function
@decorfun
def num1():
    return 10
print(num1())
