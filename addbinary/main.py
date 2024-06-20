class Solution(object):
    def addBinary(self, a, b):
        add = bin(int(a, 2) + int(b,2))
        return add.split('0b')[1]
    
c = Solution()
print(c.addBinary("1","1"))