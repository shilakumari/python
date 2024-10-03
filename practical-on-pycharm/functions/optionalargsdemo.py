def myfun(x,*args, **kwargs):
    print(x)

    for each_args in args:
        print(each_args)
    for key,value in kwargs.items():
        print(key,value)

    #Modified args
    modified_args_param=args+(50,)
    # Modified kwargs
    kwargs['id'] = 123

    myfun2(*modified_args_param,**kwargs)

def myfun2(*args, **kwargs):
    print(args)
    print(kwargs)
myfun(10, 56,8,9,9,name="Shila", salary=13456789)

