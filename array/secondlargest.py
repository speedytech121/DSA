# second largest element in array without sorting

def print2largest(arr):
        if len(arr)<2:
            return -1
        largest=second_largest=-1
        for i in arr:
            if i>largest:
                second_largest=largest
                largest=i
            if i>second_largest and i!=largest:
                second_largest=i
        return second_largest

arr=[2,5,1,3,0,33,22,11]
print(print2largest(arr))