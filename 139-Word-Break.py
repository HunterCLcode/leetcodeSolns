class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[-1] = True

        for i in range(len(dp) - 2, -1, -1):
            for word in wordDict:
                if len(word) + i < len(dp) and word == s[i:i+len(word)]: dp[i] |= dp[i+len(word)]
        return dp[0]
