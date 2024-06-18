class Solution(object):
    def searchInsert(self, nums, target):
        neg = {}
        pos={}
        if target in nums:
            return nums.index(target)
        elif target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        else:
            for x in nums:
                temp = x - target
                if temp < 0:
                    neg[x] = temp
                else:
                    pos[x] = temp
            return nums.index(min(pos))
        
c = Solution()
print(c.searchInsert([1,3,5,6], 2))
