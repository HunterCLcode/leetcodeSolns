class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min(len(s) for s in strs)

        for i in range(minLen):
            getLetter, addToOutput = strs[0][i], True
            for string in strs:
                addToOutput = False if string[i] != getLetter else addToOutput
            if not addToOutput:
                return strs[0][:i]
        return strs[0][:minLen]
