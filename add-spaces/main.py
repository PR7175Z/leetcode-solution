class Solution(object):
    def addSpaces(self, s, spaces):
        c = []
        i = 0

        for x in range(len(s)):
            if i < len(spaces) and spaces[i] == x:
                c.append(" ")
                i += 1
            
            c.append(s[x])
        return "".join(c)

s = Solution()
c = s.addSpaces('icodeinpython', [1,5,7,9])
print(c)