# The decorator to make it bold
def makebold(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<b>" + fn() + "</b>"
    return wrapper

# The decorator to make it italic
def makeitalic(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print(say())
#outputs: <b><i>hello</i></b>

# This is the exact equivalent to
def say():
    return "hello"
say = makebold(makeitalic(say))

print(say())
#outputs: <b><i>hello</i></b>