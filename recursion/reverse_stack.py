class Solution:
    li=[]
    def reverse(self,arr): 
        if(len(arr)==0):
            print(self.li)
        else:
            self.li.append(arr.pop())
            self.reverse(arr)    
        
obj=Solution()
obj.reverse([1,2,3])