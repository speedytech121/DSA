def bubblesort(arr):
    for passes in range(len(arr)-1):
        for bubble in range(len(arr)-1-passes):
            if arr[bubble+1]<arr[bubble]:
                arr[bubble+1],arr[bubble]=arr[bubble],arr[bubble+1]
            print(arr)
    print(f"bubble sort result: {arr}")

arr=[5,4,8,7,6,3,4]
bubblesort(arr)