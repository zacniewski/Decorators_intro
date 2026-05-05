class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@MyDecorator
def say_hello(name):
    print(f"Hello {name}!")

say_hello("Alice")
say_hello("Bob")

class MyDecoratorWithArgs:
    def __init__(self, arg1, arg2):
        print(f"Decorator args: {arg1}, {arg2}")
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Wrapper args: {self.arg1}, {self.arg2}")
            return func(*args, **kwargs)
        return wrapper

@MyDecoratorWithArgs("hello", "world")
def say_bye():
    print("Bye!")

say_bye()
