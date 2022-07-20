class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1ChrArr, s2ChrArr, numEqual = [0 for i in range(26)], [0 for i in range(26)], 0
        
        for i in range(len(s1)):
            s1ChrArr[ord(s1[i]) - ord('a')] += 1
            s2ChrArr[ord(s2[i])  - ord('a')] += 1
        
        for i in range(len(s1ChrArr)):
            numEqual += 1 if s1ChrArr[i] == s2ChrArr[i] else 0
        
        l = 0
        for r in range(len(s1),len(s2)):
            if numEqual == 26: return True
            
            i1, i2 = ord(s2[l]) - ord('a'), ord(s2[r]) - ord('a')
            s2ChrArr[i1] -= 1
            
            if s2ChrArr[i1] == s1ChrArr[i1]: numEqual += 1
            elif s2ChrArr[i1] + 1 == s1ChrArr[i1]: numEqual -= 1
            
            s2ChrArr[i2] += 1
            if s1ChrArr[i2] == s2ChrArr[i2]: numEqual += 1
            elif s2ChrArr[i2] - 1 == s1ChrArr[i2]: numEqual -= 1
            
            l += 1
        return numEqual == 26
