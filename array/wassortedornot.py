'''
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
'''
def CheckSorted(arr):
    length=len(arr)
    i=1
    while i<length:
        if arr[i-1]>arr[i]:
            break
        i+=1
    rotated=arr[i:]+arr[:i]

    for i in range(1,length):
        if rotated[i-1]>rotated[i]:
            return False
    return True

print(CheckSorted([3,4,5,1,2]))
print(CheckSorted([2,1,3,4]))