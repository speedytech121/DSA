
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
print(missing(sorted([1,2,3,4])))
print(missing1(sorted(arr)))



def missingNumber(a, N):
    from collections import defaultdict

    hash=defaultdict(lambda:0)

    for i in range(N - 1):
        hash[a[i]] += 1

    for i in range(1, N + 1):
        if hash[i] == 0:
            return i
    return -1

def main():
    N = 5
    a = [1, 2, 3, 4]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)

if __name__ == '__main__':
    main()


