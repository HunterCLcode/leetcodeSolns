class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      
        l, res = 0, 0
        chrCount = [0 for i in range(26)]
        maxNum = 0
        for r in range(0,len(s)):
            chrCount[ord(s[r]) - ord('A')] += 1
            while (sum(chrCount) - max(chrCount)) > k:
                chrCount[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
