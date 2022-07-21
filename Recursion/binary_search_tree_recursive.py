# Trees
# https://hackernoon.com/what-does-the-time-complexity-o-log-n-actually-mean-45f94bb5bfbf


def build_bst(my_list):

    if not my_list:
        return "No Child" 
    
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]

    print("Middle index: {}".format(middle_idx))
    print("Middle value: {}".format(middle_value)) 

    left_nodes = my_list[:middle_idx]
    right_nodes = my_list[middle_idx + 1:]

    tree_node = {
        "data": middle_value, 
        "left_child": build_bst(left_nodes),
        "right_child": build_bst(right_nodes)
        }
    
    return tree_node


# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
# print(binary_search_tree)

for i in binary_search_tree:
    print(binary_search_tree[i])

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
