'''
Example 1:
Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

Example 2:
Input: N=5, array[] = {5,4,3,2,1}
Output: 1,2,3,4,5
Explanation: After sorting the array is: 1, 2, 3, 4, 5
'''

class SelectionSort:
    def __init__(self, arr):
        self.arr=arr
        self.N= len(arr)
    
    def ssort(self):
        for i in range(self.N):
            min_index = i
            for j in range(i+1, self.N):
                if(self.arr[j]<self.arr[min_index]):
                    min_index=j
            self.arr[i],self.arr[min_index]=self.arr[min_index],self.arr[i]
        return self.arr


                    
obj=SelectionSort([13,20,46,24,1,52,20,9,1])
print(obj.ssort())
obj=SelectionSort([5,4,3,2,1])
print(obj.ssort())