class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, nz = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                # Find first non-zero and switch
                if nz < i: nz = i
                while nums[nz] == 0:
                    nz += 1
                    if nz == len(nums): return
                
                nums[i], nums[nz] = nums[nz], nums[i]
            i += 1
        
