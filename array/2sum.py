def twosum(arr,target):
    nummap = {}
    for i, num in enumerate(arr):
        complimentry = target - num
        if complimentry in nummap:
            return [i,nummap[complimentry]]
        else:
            nummap[num]=i
    return []

arr=[1,2,3,4,5,6]
print(twosum(arr,7))
