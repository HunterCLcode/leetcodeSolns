class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def DFS(i, curSum, curList):
            if curSum == target:
                res.append(curList)
                return
            elif curSum > target or i == len(candidates):
                return
        
            # Include
            DFS(i, curSum + candidates[i], curList + [candidates[i]])
            
            # Exclude and move one
            DFS(i + 1, curSum, curList)

        DFS(0, 0, [])
            
        return res
            
