# Time Complexity: O(m*n) Space Complexity: O(n)
def next_greater_element(nums1, nums2):
    output = []
    l = len(nums2)
    for num in nums1:
        indx = nums2.index(num)
        if indx!=l-1:
            for i in range(indx+1, l):
                if nums2[i]>num:
                    output.append(nums2[i])
                    break
            else:
                output.append(-1)
        else:
            output.append(-1)
    return output
       

# Time Complexity: O(m+n) Space Complexity: O(m+n)
def next_greater_element(nums1, nums2):
    stack=[]
    hashmap={}
    output=[]

    for i in reversed(nums2):
        while stack:
            if stack[-1]>i:
                hashmap[i]=stack[-1]
                stack.append(i)
                break
            else:
                stack.pop()

        if not stack:
            hashmap[i]=-1
            stack.append(i)

    for elem in nums1:
        output.append(hashmap[elem])
    
    return output






nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater_element(nums1,nums2))
nums1 = [2,4]
nums2 = [1,2,3,4]
print(next_greater_element(nums1,nums2))
