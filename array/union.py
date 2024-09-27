# Example 1:

# Input: 
# n = 5, arr1[] = {1, 2, 3, 4, 5}  
# m = 5, arr2 [] = {1, 2, 3, 6, 7}
# Output: 
# 1 2 3 4 5 6 7
# Explanation: 
# Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

# brute force
def union(arr1, arr2):
    print(sorted(set(arr1+arr2)))

def removeduplicate(arr):
    temp=[]
    for ele in arr:
        if ele not in temp:
            temp.append(ele)
    return sorted(temp)

def union1(arr1,arr2):
    arr=arr1+arr2
    print(removeduplicate(arr))

arr1 =[-8, -3, -3, -2, 0, 1, 2, 2, 6]
arr2 = [-9, -9, 0]

union(arr1,arr2)
union1(arr1,arr2)