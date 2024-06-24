class Solution(object):
    def reverse(self, x):
        h = 1
        if(x<0):
            x = abs(x)
            h = -1
        

        x = str(x)
        s = 0
        for y in range(len(x)-1, -1, -1):
            s += int(x[y]) * 10**y

        if s>(2**31):
            return 0
        return s*h
    

s = Solution()
print(s.reverse(1534236469))