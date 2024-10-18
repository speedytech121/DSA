def longestconsecutive(arr):
    num_set=set(arr)
    longest=0
    for n in arr:
        if n-1 not in num_set:
            length=1

            while n+length in num_set:
                length+=1
            longest = max(longest,length)
    return longest

arr=[100,4,200,1,2,3]
arr1=[0,3,7,2,5,8,4,6,0,1]
arr2=[9,1,4,7,3,-1,0,5,8,-1,6]
print(longestconsecutive(arr))
print(longestconsecutive(arr1))
print(longestconsecutive(arr2))