class floorceil:
    def __init__(self, arr, target):
        self.arr=arr
        self.target=target
        self.lower=0
        self.upper=0

    def lowerbound(self):
        low=0
        high=len(self.arr)-1
        while(low<=high):
            mid=(low+high)//2
            if self.arr[mid]<=self.target:
                self.lower=arr[mid]
                low=mid+1
            else:
                high=mid-1
        return self.lower
     
    def upperbound(self):
        low=0
        high=len(self.arr)-1
        while(low<=high):
            mid=(low+high)//2
            if self.arr[mid]>=self.target:
                self.upper=arr[mid]
                high=mid-1
            else:
                low=mid+1
        return self.upper

arr=[3, 4, 4, 7, 8, 10]
target=5
obj=floorceil(arr,target)
print(f"floor value and ceil value is : {obj.lowerbound() , obj.upperbound()}")

arr=[3, 4, 4, 7, 8, 10]
target=8
obj=floorceil(arr,target)
print(f"floor value and ceil value is : {obj.lowerbound() , obj.upperbound()}")

