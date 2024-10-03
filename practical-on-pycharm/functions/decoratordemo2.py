#create hello(name) function and decorator that add "How are you"
def decor1(fun):
    def inner(n):
        result = fun(n)+" How are you"
        return result
    return inner

@decor1
def hello(name):
    return "Hello "+name

print(hello("Shila"))

#Decorator to add two numbers
def decor2(fun):
    def inner(x,y):
        result = fun(x,y)
        result =int(x+y)
        return result
    return inner

@decor2
def s1(x,y):
    return x,y
print(s1(4,5))
