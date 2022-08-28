class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # One to one mapping
        mapChrS = dict()
        mapChrT = dict()
        for i in range(len(s)):
            if s[i] not in mapChrS:
                mapChrS[s[i]] = t[i]
            if t[i] not in mapChrT:
                mapChrT[t[i]] = s[i]
            if mapChrS[s[i]] != t[i] or mapChrT[t[i]] != s[i]: return False
        return True
