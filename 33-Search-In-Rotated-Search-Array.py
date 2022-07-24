class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # Check for rotation
        if nums[-1] < nums[0]:
            
            # Find rotation spot by finding first integer that is lower than nums[0]
            l = 1
            newR = r
            
            while l <= r:
                m = (l + r)//2
                
                if nums[m] < nums[0]:
                    newR = min(newR, m)
                    r = m - 1
                else:
                    l = m + 1
            # Get new bounds
            if target < nums[0]:
                l, r = newR, len(nums) - 1
            else:
                l, r = 0, newR - 1
        
        # Perform binary search
        while l <= r:
            m = (l + r)//2
            
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
                
