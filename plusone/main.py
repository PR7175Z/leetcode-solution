
class Solution(object):
    def plusOne(self, digits):
        nums=0
        x = len(digits)
        for i in digits:
            x-=1
            nums += i*(10**x)

        nums = str(nums+1)
        d = [int(x) for x in nums]
        return d
    
c = Solution()
print(c.plusOne([1,9,9]))