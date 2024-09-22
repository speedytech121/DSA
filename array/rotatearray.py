def rotatearray(arr,k):
    r_index=-(k)
    li=[]
    for i in range(k):
        li.append(arr[r_index])
        r_index += 1

    for i in range(k+1):
        li.append(arr[i])
    
    return li

arr=[1,2,3,4,5,6,7]
k=3 

print(rotatearray(arr,k))