# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
    if n < 0:
        raise ValueError("Inputs 0 or greater only!")
    
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result + n
    
print(sum_digits(12))
# 1 + 2
# 3
print(sum_digits(552))
# 5 + 5 + 2
# 12
print(sum_digits(123456789))
# 1 + 2 + 3 + 4...
# 45