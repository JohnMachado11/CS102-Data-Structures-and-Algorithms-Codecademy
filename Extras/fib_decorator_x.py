from functools import wraps


def decorator_outside(*args):
    def decorator_inside(func):
        @wraps(func)
        def wrapper():
            text = func(*args)
            return text
        return wrapper
    return decorator_inside


@decorator_outside(1,4) # "Fxxxnacci"
def fib_text(*args):
    start = args[0]
    end = args[1]
    fib = ["F", "i", "b", "o", "n", "a", "c", "c", "i"]
    
    for i in range(start, end):
        if fib[-1] == "x":
            return ''.join(fib)
        fib[i] = "x"

    return ''.join(fib)

print(fib_text())

# @decorator_outside(0,10) # "xxxxxxxxx"
# @decorator_outside(5,15) # "Fibonxxxx"
# @decorator_outside(0,0) # "Fibonacci"

