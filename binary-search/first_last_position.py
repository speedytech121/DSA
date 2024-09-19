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


arr=[5,7,7,8,8,10]
target=8
lower=find_lowerbound(arr,target)
upper=find_upperbound(arr,target)
print(f"result {[lower,upper]}")


arr = [5, 7, 7, 8, 8, 10]
target = 6
lower = find_lowerbound(arr, target)
upper = find_upperbound(arr, target)
print(f"result [{lower}, {upper}]")
