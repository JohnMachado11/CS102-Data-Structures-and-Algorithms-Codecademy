# importing heap class
from max_heap import MaxHeap 

# an instance of maxHeap to use
max_heap = MaxHeap()

# the internal list for our example
max_heap.heap_list = [None, 99, 22, 61, 10, 21, 13, 23]
print(max_heap.heap_list)


# example of how to use the helper methods:
print("the parent index of 4 is:")
print(max_heap.parent_idx(4))
print("the left child index of 3 is:")
print(max_heap.left_child_idx(3))

# now it's your turn!
# replace 'None' below using the correct helper methods and indexes
idx_2_left_child_idx = max_heap.left_child_idx(2)
print("The left child index of index 2 is:")
print(idx_2_left_child_idx)
print("The left child element of index 2 is:")
# uncomment the line below to see the result in your console!
print(max_heap.heap_list[idx_2_left_child_idx])

idx_3_parent_idx = max_heap.parent_idx(3)
print("The parent index of index 3 is:")
print(idx_3_parent_idx)
print("The parent element of index 3 is:")
# uncomment the line below to see the result in your console!
print(max_heap.heap_list[idx_3_parent_idx])

idx_3_right_child_idx = max_heap.right_child_idx(3)
print("The right child index of index 3 is:")
print(idx_3_right_child_idx)
print("The right child element of index 3 is:")
# uncomment the line below to see the result in your console!
print(max_heap.heap_list[idx_3_right_child_idx])
