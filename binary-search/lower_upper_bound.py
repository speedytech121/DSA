# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.
# lower bound of x means the first or smalest index on which value is  greater or equal to x 
# arr[ind]>=x

def find_lowerbound(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    # Check if the element at result index is the target
    if result != -1 and arr[result] != target:
        return -1
    return result

def find_upperbound(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    # Check if the element at result index is the target
    if result != -1 and arr[result] != target:
        return -1
    return result

# ----------------lower bound Test cases
arr = [1, 2, 2, 3, 3, 5]
target = 2
print(find_lowerbound(arr, target))  # Output should be 1

arr = [1, 2, 2, 3]
target = 2
print(find_lowerbound(arr, target))  # Output should be 1

# ---------------upper bound Test cases
arr = [1, 2, 2, 3, 3, 5]
target = 2
print(find_upperbound(arr, target))  # Output should be 1

arr = [1, 2, 2, 3]
target = 2
print(find_upperbound(arr, target))  # Output should be 1
