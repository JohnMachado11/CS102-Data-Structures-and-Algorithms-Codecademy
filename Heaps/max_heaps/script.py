# import random number generator
from random import randrange
# import heap class
from max_heap import MaxHeap 

# make an instance of MaxHeap
max_heap = MaxHeap()

# populate max_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
    max_heap.add(el)
