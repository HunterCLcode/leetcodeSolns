class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cur, res = 1, 0
        
        for letter in columnTitle[::-1]:
            res += (ord(letter) - ord('A') + 1) * cur
            cur *= 26
        
        return res
            
