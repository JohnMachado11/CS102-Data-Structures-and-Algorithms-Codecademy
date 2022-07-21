
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))

# 0 1 1 2 3 5
# 0 + 1 = 1
# 1 + 1 = 2
# 2 + 1 = 3
# 3 + 2 = 5

# Algorithms with running time O(2^N) are often recursive algorithms
# that solve a problem of size N by recursively solving two smaller problems of size N-1.
fibonacci_runtime = "2^N"