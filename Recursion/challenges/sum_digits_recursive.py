# Linear - O(N), where "N" is the number of digits in the number

def sum_digits(n):
    
    if type(n) == int:
        if n < 0:
            raise ValueError("Inputs 0 or greater only!")
    
    if type(n) != list:
        split_digits = [int(x) for x in str(n)]
    else:
        split_digits = n[0:]
    
    if len(split_digits) == 1:
        return split_digits[0]
    else:
        last_num = split_digits.pop(-1)
        return last_num + sum_digits(split_digits)    

print(sum_digits(12)) # 3
print(sum_digits(552)) # 12
print(sum_digits(123456789)) # 45