
# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
    if len(my_list) == 0:
        return None

    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[ : mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

    return tree_node

def depth(tree):
    
    if not tree["left_child"]:
        return 1

    return 1 + depth(tree["left_child"])



tree_level_1 = build_bst([1])
print(depth(tree_level_1)) # 1

tree_level_2 = build_bst([1, 2, 3])
print(depth(tree_level_2)) # 2

tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 
print(depth(tree_level_4)) # 4