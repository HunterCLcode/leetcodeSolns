class Solution:
    def numDecodings(self, s: str) -> int:
        letterMap = {(i + 1) : chr(i + 65) for i in range(0,26)}
        prev1, prev2 = [1 if int(s[-1]) in letterMap else 0, 1]

        for i in range(len(s) - 2, -1, -1):
            current = 0
            if int(s[i]) in letterMap:
                current += prev1

                if int(s[i:i+2]) in letterMap:
                    current += prev2
            prev2 = prev1
            prev1 = current
        return prev1
