"""The previous example, using the decorator syntax:

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")

another_stand_alone_function()
#outputs:
#Before the function runs
#Leave me alone
#After the function runs

Yes, that's all, it's that simple. @decorator is just a shortcut to:

another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
"""
"""Decorators are just a pythonic variant of the decorator design pattern.
There are several classic design patterns embedded in Python to ease development, like iterators.
Of course, you can cumulate decorators:"""


def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper


def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>

#Using the Python decorator syntax:

@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>

#The order you set the decorators MATTERS:

@ingredients
@bread
def strange_sandwich(food="--ham--"):
    print(food)

strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~