def two_sum(arr, target):
    num_map={}

    for i in range(len(arr)):
        compliment=target-arr[i]
        if compliment in num_map:
            return [i,num_map[compliment]]
        num_map[arr[i]]=i
    return []


arr=[1,2,3,4,5,6]
print(two_sum(arr,55))
