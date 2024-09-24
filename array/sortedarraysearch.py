def sorted_array_search(arr, low, high, target):
    if low>high:
        return None
    
    mid=(low+high)//2
    if arr[mid]==target:
         return mid
    elif arr[mid]>target:
        return sorted_array_search(arr,low,mid-1,target)
    else:
        return sorted_array_search(arr,mid+1,high,target)
    
arr=[1,2,3,4,5,6,7]
print(sorted_array_search(arr,0,len(arr)-1,3))
print(sorted_array_search(arr,0,len(arr)-1,9))