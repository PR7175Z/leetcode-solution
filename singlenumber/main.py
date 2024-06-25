

class Solution(object):
    def singleNumber(self, nums):
        for x in nums:
            c = 0
            for y in nums:
                if(x == y):
                    c += 1

            if(c == 1):
                return x
            
c = Solution()
print(c.singleNumber([4,1,2,1,2]))