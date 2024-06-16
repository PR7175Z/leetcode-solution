class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    

c = Solution()
print(c.removeDuplicates([1,2,3,1,1,2,2]))
    