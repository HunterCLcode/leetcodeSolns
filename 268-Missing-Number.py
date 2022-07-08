
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sum solution
        # return sum(range(0,len(nums) + 1)) - sum(nums)
        
        # XOR soln.
        e = len(nums)
        
        for i in range(0,len(nums)):
            e ^= i ^ nums[i]
        return e
