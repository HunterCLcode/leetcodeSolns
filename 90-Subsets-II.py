class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        subset = []
        def DFS(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # Include
            subset.append(nums[i])
            DFS(i + 1)
            
            # Exclude
            subset.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            DFS(i + 1)
            
        DFS(0)
        return res
