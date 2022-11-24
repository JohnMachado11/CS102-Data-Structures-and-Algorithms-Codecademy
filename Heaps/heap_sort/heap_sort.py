from max_heap import MaxHeap 

def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for idx in lst:
        max_heap.add(idx)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
    return sort

my_list = [99, 22, 61, 10, 21, 13, 23]
sorted_list = heapsort(my_list)
print(sorted_list)