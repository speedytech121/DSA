# largest odd number in a string

def LargestOdd(num:str):
    n=len(num)-1
    while(n>=0):
        if int(num[n])%2!=0:
            return num[:n+1]
        n-=1
    return "None"


print(LargestOdd("52"))
print(LargestOdd("4206"))
print(LargestOdd("35427"))