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


def print_maxsubarray_sum(arr):
    currsum=maxsum=count=0
    ansstart=ansend=-1
    for i in range(len(arr)):
        if arr[i]<0:
            count+=1
        if currsum == 0:
            start = i
        currsum=currsum+arr[i]
        if currsum>maxsum:
            maxsum=currsum
            ansstart = start
            ansend = i
        if currsum<0:
            currsum=0
        if count==len(arr):
            return max(arr)
        
    print(arr[ansstart:ansend+1])
    return maxsum

arr=[-2,1,-3,4,-1,2,1,-5,4]
arr1=[-2,-1,-5]
print(maximum_subarray_sum(arr))
print(maximum_subarray_sum(arr1))
print_maxsubarray_sum(arr)
print_maxsubarray_sum(arr1)