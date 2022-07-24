class Solution:
    def findMin(self, nums: List[int]) -> int:
        minPos = 0
        # Binary search for rotated value if rotation detected
        if nums[-1] < nums[0]:
            l, r = 1, len(nums) - 1
            minPos = r
            
            while l <= r:
                m = (l + r)// 2
                
                if nums[m] < nums[0]:
                    minPos = m
                    r = m - 1
                else:
                    l = m + 1
        return nums[minPos]
                    
