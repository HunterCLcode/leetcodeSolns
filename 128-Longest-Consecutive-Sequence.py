class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hset, res = set(nums), 0
        for i in nums:
            if not (i - 1) in hset:
                cur, seq = i + 1, 1
                while cur in hset:
                    seq += 1
                    cur += 1
                res = max(res,seq)
        return res
