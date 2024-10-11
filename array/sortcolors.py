class Solution:
    def sortColors(self, nums) -> None:
        red_count = nums.count(0)
        white_count = nums.count(1)
        blue_count = nums.count(2)

        for i in range(red_count):
            nums[i]=0
        for j in range(red_count, red_count + white_count):
            nums[j]=1
        for k in range(red_count + white_count, red_count + white_count + blue_count):
            nums[k]=2
        return nums


obj=Solution()
print(obj.sortColors([1,2,0,1,2,1,0]))