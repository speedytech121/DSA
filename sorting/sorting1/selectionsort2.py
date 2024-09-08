# kth smallest in the array
# Problem: Use selection sort to find the k-th smallest or largest element in an array.
# Input: An array of integers [7, 10, 4, 3, 20, 15], and k = 3.
# Output: The 3rd smallest element is 7.


def kth_smallest(arr,pos):
    flag=0
    for i in range(pos):
        minindex=i
        flag+=1
        for j in range(i+1, len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
        
    print(f"smallest element at position {pos} is: {arr[pos-1]}")
    
kth_smallest([7, 10, 4, 3, 20, 15],2)