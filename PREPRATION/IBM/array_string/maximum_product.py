def maximum_product(arr):
    if len(arr)<2:
       print("array must have at least two numbers")
    arr.sort()
    print(arr)
    # max product can be fromthe top 2 elements or bottom 2 elements (for negatives)
    return max(arr[-1]*arr[-2], arr[0]*arr[1])



arr = [4,2,5,3]
arr1 = [5,5]
arr2 = [5,3]
arr3 = [-10, -3, 5, 4,-2]
print(maximum_product(arr))
print(maximum_product(arr1))
print(maximum_product(arr2))
print(maximum_product(arr3))

