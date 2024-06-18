class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        return len(s.split()[-1])
    
c = Solution()
print(c.lengthOfLastWord("   fly me   to   the moon  "))