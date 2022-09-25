class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        first1, first2 = 0, 0
        notFirst1, notFirst2 = 0, 0
        
        for i in range(0, len(nums) - 1):
            firstHolder, notFirstHolder = max(nums[i] + first2, first1), max(nums[i + 1] + notFirst2, notFirst1)
            first2, notFirst2 = first1, notFirst1
            first1, notFirst1 = firstHolder, notFirstHolder
        return max(first1, notFirst1)
            
            
