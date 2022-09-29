class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(0, len(s)):

            # Odd
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                count += 1
                l, r = l - 1, r + 1

            # Even
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                count += 1
                l, r = l - 1, r + 1
        return count
