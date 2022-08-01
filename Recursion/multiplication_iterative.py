
def multiplication(num_1, num_2):
    result = 0
    for count in range(0, num_2):
        result += num_1
    return result


print(multiplication(3, 7))
# 21
print(multiplication(5, 5))
# 25
print(multiplication(0, 4))
# 0