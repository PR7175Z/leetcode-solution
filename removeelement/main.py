class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        i = 0
        if val in nums:
            for x in nums:
                if x != val:
                    nums[i] = x
                    i=i+1
            k = i
        else:
            k = len(nums)
        return k
    
c = Solution()
print(c.removeElement([2], 3))

