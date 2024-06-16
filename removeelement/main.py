class Solution(object):
    def removeElement(self, nums, val):
        nums.remove(val)
        for x in nums:
            if x == val:
                nums.remove(x)

        k = len(nums)
        return k
    
c = Solution()
print(c.removeElement([1,1,2,1,2,3,4,5,5], 1))

