class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        def isLetter(c):
            return ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122
        
        output, index = 0, len(s)-1
        
        while index >= 0 and not isLetter(s[index]):
            index -= 1
        
        while index >= 0 and isLetter(s[index]):
            output += 1
            index -= 1
        return output
