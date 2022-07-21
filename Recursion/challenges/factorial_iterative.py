def factorial(n):
    if n < 0:
        raise ValueError("Inputs 0 or greater only!") 
    if n <= 1:
        return 1

    num = 1
    for i in range(2, n + 1):
        num *= i

    return num

print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)