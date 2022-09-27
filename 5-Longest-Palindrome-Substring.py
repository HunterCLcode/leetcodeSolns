class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        
        for i in range(0, len(s) - 1):
            
            # Odd
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res): res = s[l:r + 1]
                l, r = l - 1, r + 1
            
            # Even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res): res = s[l:r + 1]
                l, r = l - 1, r + 1
            
        return res
