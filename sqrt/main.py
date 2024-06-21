import math

class Solution(object):
    def mySqrt(self, x):
        return (int(math.floor(math.sqrt(x))))

c= Solution()
print(c.mySqrt(20))