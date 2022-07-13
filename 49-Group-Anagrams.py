class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            hmap[tuple(self.getCharCount(s))].append(s)
        return hmap.values()
    
    def getCharCount(self, s):
        chars = [0 for i in range(26)]
        for i in s:
            chars[ord(i)-97] += 1
        return chars
