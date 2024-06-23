class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(letter for letter in s if letter.isalnum())

        if s.lower() == s[::-1].lower():
            return True
        else:
            return False
        
c = Solution()
print(c.isPalindrome("race a car"))