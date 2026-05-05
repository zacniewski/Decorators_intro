"""Best practices while using decorators

    They are new as of Python 2.4, so be sure that's what your code is running on.
    Decorators slow down the function call. Keep that in mind.
    You can not un-decorate a function.
    There are hacks to create decorators that can be removed but nobody uses them.
    So once a function is decorated, it's done. For all the code.
    Decorators wrap functions, which can make them hard to debug.

Python 2.5 solves this last issue by providing the functools module including functools.wraps that copies the name,
module and docstring of any wrapped function to it's wrapper. Fun fact, functools.wraps is a decorator :-)
"""

# For debugging, the stacktrace prints you the function __name__
def foo():
    print("foo")

print(foo.__name__)
#outputs: foo

# With a decorator, it gets messy
def bar(func):
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__)
#outputs: wrapper

# "functools" can help for that

import functools

def bar(func):
    # We say that "wrapper", is wrapping "func"
    # and the magic begins
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__)
#outputs: foo