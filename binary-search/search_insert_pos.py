def search_insert_pos(arr,target):
    low=0
    high=len(arr)-1
    position=len(arr)

    while (low<=high):
        mid = (low+high)//2
        if arr[mid]>=target:
            position=mid
            high=mid-1
        else:
            low=mid+1
        
    return position

print(search_insert_pos([1,2,4,5,6],3))
print(search_insert_pos([1,3,5,6],5))