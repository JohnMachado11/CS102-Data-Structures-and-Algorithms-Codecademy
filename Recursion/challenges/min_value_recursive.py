
def find_min(my_list):
    
    if not my_list:
        return None
    
    if len(my_list) == 1:
        return my_list[0]
    else:
        if my_list[0] < my_list[-1]:
            my_list.pop(-1)
        else:
            my_list.pop(0)
    
    return find_min(my_list)


print(find_min([42, 17, 2, -1, 67]))
# -1
print(find_min([]))
# None
print(find_min([13, 72, 19, 5, 86]))
# 5