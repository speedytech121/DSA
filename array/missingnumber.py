
# print((n*(n-1))//2) sum of first n-1 integer numbers
# print((n*(n+1))//2) sum of first n integer numbers


def missing(arr):
    expected=0
    for n in arr:
        if n!=expected:
            return expected
        expected+=1
    return -1

def missing1(arr):
    n=len(arr)
    # sum of first n integer numbers (n*(n+1))//2
    expected_sum = (n*(n+1))//2
    actual_sum = sum(e for e in arr)
    return expected_sum-actual_sum


arr = [9,6,4,2,3,5,7,0,1]
print(missing(sorted(arr)))
print(missing1(sorted(arr)))


