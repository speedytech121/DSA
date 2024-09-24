def leftoccurence(arr,target):
    index=-1
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            index=mid
            high=mid-1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return index

def rightoccurence(arr,target):
    index=-1
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            index=mid
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return index


def count(arr,target):
    left=leftoccurence(arr,target)
    if left==-1:
        return (-1,-1)
    right=rightoccurence(arr,target)
    result=(right-left)+1
    return result

arr = [2, 4, 6, 8, 8, 8, 11, 13]
target=8
print(count(arr,target))