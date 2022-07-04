class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers
        l = 0
        r = len(s)-1
        while l < r:
            if not self.isAlphaNumerical(s[l]):
                l += 1
            elif not self.isAlphaNumerical(s[r]):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def isAlphaNumerical(self, c):
        return (ord(c) >= 48 and ord(c) <= 57 or
                ord(c) >= 65 and ord(c) <= 90 or
                ord(c) >= 97 and ord(c) <= 122)