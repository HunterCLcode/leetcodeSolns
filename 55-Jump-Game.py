class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] + j >= i:
                i = j
        
        return i == 0
