class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = current = nums[0]
        for i in range(1,len(nums)):
            current = nums[i] if current + nums[i] < nums[i] else nums[i] + current
            output = max(current, output)
        return output
                    
                
        