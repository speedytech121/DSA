#  Selection Sort in Descending Order

def SelectionSort(arr):
    for i in range(len(arr)):
        maxindex=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[maxindex]:
                maxindex=j
        arr[i],arr[maxindex]=arr[maxindex],arr[i]
    print(arr)

SelectionSort([1,2,3,4,5])