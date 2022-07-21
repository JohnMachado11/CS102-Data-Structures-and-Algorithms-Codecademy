
def fibonacci(n):
    if n < 0:
        raise ValueError("Input 0 or greater only!")
    if n <= 1:
        return n

    fib_list = [1, 2]
    for i in range(3, n + 1):
        if len(fib_list) < 3:
            fib_list.append(i)
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])

    fib_list.insert(0, 1)
    fib_list.insert(0, 0)

    return f"""
                Fibonacci Sequence List: {fib_list} 
                Value of Index {n}: {fib_list[n]}
            """

# 0 1 1 2 3 5 

print(fibonacci(7))
print(fibonacci(3))
print(fibonacci(0))