class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, cur, ncur = min(nums), float('-inf'), float('-inf')

        for num in nums:
            if not num: cur, ncur = 0, 0
            elif num > 0:
                cur = cur * num if cur != float('-inf') and cur != 0 else num
                ncur = ncur * num
            elif num < 0:
                holder = cur
                cur = ncur * num * -1
                ncur = holder * num * -1 if holder != float('-inf') and holder != 0 else num * -1

            res = max(cur, res)
        return res
