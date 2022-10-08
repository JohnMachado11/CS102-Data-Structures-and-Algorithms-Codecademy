def qs(arr):
    if len(arr) <= 1:
        return arr
    
    smaller = []
    larger = []
    
    pivot = 0
    pivot_element = arr[pivot]
    
    for i in range(1, len(arr)):
        if arr[i] > pivot_element:
            larger.append(arr[i])
        else:
            smaller.append(arr[i])
    
    sorted_smaller = qs(smaller)
    sorted_larger = qs(larger)
    
    return sorted_smaller + [pivot_element] + sorted_larger

arr = [22, 55, 8, 89, 101, 22, 4, 92]
print(qs(arr))