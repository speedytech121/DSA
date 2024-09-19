# ["apple", "orange", "banana", "grape"] selection sort on strings


# This implementation compares strings lexicographically, 
# and after sorting, the list is in alphabetical order.

def selection_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = ["apple", "orange", "banana", "grape"]
sorted_arr = selection_sort_strings(arr)
print(sorted_arr)
