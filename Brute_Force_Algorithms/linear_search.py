

def linear_search(search_list, target_value):

    for i in range(len(search_list)):
        
        if search_list[i] == target_value:
            return i

    raise ValueError("{} not in list".format(target_value))


values = [54, 22, 46, 99]

print(linear_search(values, 22)) # 1
print(linear_search(values, 99)) # 3
print(linear_search(values, 199)) # Not in list


# Alternate way to call function
try:
    result = linear_search(values, 22)
    result = linear_search(values, 212)
    print(result)
except ValueError as error_message:
    print("{}".format(error_message))