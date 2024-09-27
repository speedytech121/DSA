def findMaxConsecutiveOnes(arr):
    count=0
    max=0

    for one in arr:
        if one==1:
            count+=1

        elif one==0:
            if max<count:
                max=count
            count=0

    '''checking the last sequence of consecutive ones after the loop finishes.'''
    if max < count:
        max=count
    
    print(max)

    


arr=[1,1,0,1,1,1,0,1,1,1,1]
findMaxConsecutiveOnes(arr)

arr=[1,1,1,1,1,1]
findMaxConsecutiveOnes(arr)