'''
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
# iterative approach
def BinarySearch(arr, target):
    start=0
    stop=len(arr)-1
    while(start<=stop):
        mid=(start+stop)//2
        if(arr[mid]==target):
            return mid
        if(arr[mid]>target):
            stop=mid-1
        else:
            start=mid+1

# recursive approach
def binary_search(arr, low, high, target):
    if low>high:
        return -1
    mid = (low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,low,mid-1,target)
    else:
        return binary_search(arr,mid+1,high,target)
    
a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
print(binary_search(a,0,len(a)-1,target))
