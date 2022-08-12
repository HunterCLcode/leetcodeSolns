class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def DFS(perm, curNums):
            if len(perm) == len(nums):
                res.append(perm)
                return
            
            for i in range(0,len(curNums)):
                holder = curNums.copy()
                holder.pop(i)
                DFS(perm + [curNums[i]], holder)
            return
            
        
        DFS([], nums)
        return res
