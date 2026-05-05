class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """I am a property!"""
        print("Getting value")
        return self._value

    @value.setter
    def value(self, new_value):
        print("Setting value")
        self._value = new_value

    @staticmethod
    def static_method():
        print("I am a static method, I don't care about the instance or the class")

    @classmethod
    def class_method(cls):
        print(f"I am a class method of {cls}")

obj = MyClass(10)
print(obj.value)
obj.value = 20
MyClass.static_method()
MyClass.class_method()
