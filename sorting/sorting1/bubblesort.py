# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52

def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if(arr[j+1]<arr[j]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
    print(arr)
    
BubbleSort([13,46,24,52,20,9])