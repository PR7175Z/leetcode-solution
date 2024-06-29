class Solution(object):
    def divide(self, dividend, divisor):
        # Handling edge cases where result could overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Calculate sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        # Use absolute values for calculation
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize quotient
        quotient = 0
        
        # Subtract divisor from dividend until dividend is less than divisor
        while dividend >= divisor:
            # Determine the highest multiple of divisor that fits into the dividend
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract that multiple from dividend and add multiple to quotient
            dividend -= temp
            quotient += multiple
        
        # Apply sign to quotient
        if negative:
            quotient = -quotient
        
        # Handle overflow
        return min(max(-2**31, quotient), 2**31 - 1)
    
c = Solution()
print(c.divide(-2147483648,-1))