
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

c = Solution()
print(c.majorityElement([1,1,1,1,3,2,3]))