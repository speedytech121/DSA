def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k=0,0,0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1
        
        while i<len(left_arr): #means it didnt complete all its element in previous loop
            arr[k]=left_arr[i]
            i+=1
            k+=1

        while j<len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1
        
    return arr

print(merge_sort([6,7,5,4,2,8,1]))
print(merge_sort([6,7]))
print(merge_sort([6]))