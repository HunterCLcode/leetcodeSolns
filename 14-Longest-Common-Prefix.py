class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output, minLen = 0, min(len(s) for s in strs)

        for i in range(minLen):
            getLetter, addToOutput = strs[0][i], True
            for string in strs:
                addToOutput = False if string[i] != getLetter else addToOutput
            output += 1 if addToOutput else 0
            if not addToOutput:
                break
        return strs[0][:output]
