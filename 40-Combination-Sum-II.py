class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def DFS(cur, nums, sumCur):
            if sumCur == target:
                res.append(cur)
                return
            if sumCur > target or not len(nums):
                return
            
            # Include current
            num = nums.pop()
            DFS(cur + [num], nums[:], sumCur + num)
            
            # Exclude current
            while len(nums) and num == nums[-1]:
                nums.pop()
            DFS(cur, nums[:], sumCur)
        
        DFS([], candidates[:], 0)
        return res
