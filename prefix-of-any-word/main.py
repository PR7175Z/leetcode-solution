class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        for index, value in enumerate(sentence.split(" ")):
            if value.startswith(searchWord):
                return index+1
            
        return -1


c = Solution()

print(c.isPrefixOfWord("hellohello hellohellohello", "ell"))