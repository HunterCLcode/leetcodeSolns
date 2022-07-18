class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Both pointers are inclusive and can point at the same var. R will always be at or greater than L
        l, r, res = 0, 0, 0
        
        while r < len(s):
            
            # Increase R until it includes a duplicate
            while r < len(s) and not s[r] in s[l:r]:
                r += 1
            res = max(r - l, res)
            
            # Increase L until we don't include the duplicate we found
            while r < len(s) and s[l] != s[r]:
                l += 1
            l += 1
        return res
