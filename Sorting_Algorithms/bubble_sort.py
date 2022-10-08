
def bubble_sort(arr):
    arr_size = len(arr) 
    idx = 0
    for i in range(arr_size - 1):
        for j in range(i + 1, arr_size): # 1 - 5
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

nums = [5, 2, 9, 1, 5, 6]
bubble_sort(nums)
print(nums)
