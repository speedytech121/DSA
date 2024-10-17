def maximum_subarray_sum(arr):
    currsum=maxsum=count=0
    for i in range(len(arr)):
        if arr[i]<0:
            count+=1
        currsum=currsum+arr[i]
        if currsum>maxsum:
            maxsum=currsum
        if currsum<0:
            currsum=0
        if count==len(arr):
            return max(arr)
    return maxsum

arr=[-2,1,-3,4,-1,2,1,-5,4]
arr1=[-2,-1,-5]
print(maximum_subarray_sum(arr))
print(maximum_subarray_sum(arr1))