# largest element in an array

# approach 1: sort and return last element

def selectionsort(arr):
    for i in range(len(arr)-1):
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr
                
def largest(arr):
    arr=selectionsort(arr)
    print(f"largetst element in array is: {arr[-1]}")

def largestwithoutsort(arr):
    largest=-1
    for i in arr:
        if i>largest:
            largest=i
    print(largest)
    
arr=[2,5,1,3,0,33,22,11]
largestwithoutsort(arr)