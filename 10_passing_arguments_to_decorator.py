"""Great, now what would you say about passing arguments to the decorator itself?
Well this is a bit twisted because a decorator must accept a function as an argument and therefore,
you cannot pass the decorated function arguments directly to the decorator.
Before rushing to the solution, let's write a little reminder:
"""

# Decorators are ORDINARY functions
def my_decorator(func):
    print("I am a ordinary function")
    def wrapper():
        print("I am function returned by the decorator")
        func()
    return wrapper

# Therefore, you can call it without any "@"

def lazy_function():
    print("zzzzzzzz")

decorated_function = my_decorator(lazy_function)
#outputs: I am a ordinary function

# It outputs "I am a ordinary function", because that's just what you do:
# calling a function. Nothing magic.

@my_decorator
def lazy_function():
    print("zzzzzzzz")

#outputs: I am a ordinary function