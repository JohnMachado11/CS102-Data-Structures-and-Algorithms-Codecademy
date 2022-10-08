

def insertion_sort(arr):
    for i in range(len(arr)): 
        j = i 
        while j and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j - 1

nums = [5, 2, 3, 11, 0, 29]

insertion_sort(nums)
print(nums)