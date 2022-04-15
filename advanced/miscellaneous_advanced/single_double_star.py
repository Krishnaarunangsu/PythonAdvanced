# The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions as described in the
# section more on defining functions in the Python documentation.

# The *args will give you all function parameters as a tuple:

def foo(*args):
    """Single star"""
    for a in args:
        print(f'Argument in argument list is:{a}')


foo(1)
print("######################")
foo(2, 3, 7)


# The **kwargs will give you all keyword arguments
# except for those corresponding to a formal parameter as a dictionary.

def bar(**kwargs):
    """Double star
    :rtype: object
    """
    for a in kwargs:
        print(f'Key is: {a} and the value is:{kwargs[a]}')


bar(name="one", age=27)
print("###Dictionary Printing###")
bar(dictionary1={"a": 1, "b": "Krishna"})


# Both idioms can be mixed with normal arguments to allow a set of fixed and some variable arguments:

def foo(kind, *args, **kwargs):
    pass


# It is also possible to use this the other way around:

def foo(a, b, c):
    print(a, b, c)


obj = {'b': 10, 'c': 'lee'}

foo(100, **obj)


# # 100 10 lee

def my_fun(arg1, *argv):
    """Single Star
    :type arg1: object
    """
    print(f'First Argument is:{arg1}')
    print("Arguments are as in the following")
    for a in argv:
        print(f'The argument is:{a}')


my_fun("Krishna", "Narayan", "Jagannath", "Tirupati")


def my_fun_extra(arg, *argv, **kwargs):
    """No Star,Single and Double star"""
    print(f'Single argument is {arg}')
    for a in argv:
        print(f'The argument is:{a}')

    for b in kwargs:
        print(f'The argument is:{kwargs[b]}')


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
# myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)

arg_1 = "Krishna"

my_fun_extra(arg_1, args, kwargs)
