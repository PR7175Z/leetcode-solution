class Solution(object):
    def divide(self, dividend, divisor):
        inidiv = dividend
        x=0
        if dividend == divisor: return 1
        
        if abs(divisor) == 1:
            x = abs(dividend)
        else:
            while abs(dividend) >= abs(divisor):
                dividend = abs(dividend)-abs(divisor)
                x += 1

        if inidiv < 0:
            x = -x
        if divisor < 0:
            x = -x

        if x > (2**31)-1:
            return (2**31)-1
        elif x < -(2**31):
            return -(2**31)

        return x
    
c = Solution()
print(c.divide(-2147483648,-1))