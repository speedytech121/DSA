def findsingle(arr):
    d={}
    for ele in arr:
        d[ele]=d.get(ele,0)+1
    print(next(key for key, value in d.items() if value==1))

arr=[4,1,2,1,2]
findsingle(arr)