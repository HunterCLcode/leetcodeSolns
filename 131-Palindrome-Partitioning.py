class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
                
        def DFS(cur, i):
            if i == len(s):
                if cur[-1] == cur[-1][::-1]: res.append(cur)
                return
            
            # Exclude partition of 2 letters (Don't combine them)
            if cur[-1] == cur[-1][::-1]:
                DFS(cur + [s[i]], i + 1)
            
            # Include partition of 2 letters (Combine them)
            cur[-1] = cur[-1] + s[i]
            DFS(cur[::], i + 1)
            
            
        
        DFS([s[0]], 1)
        return res
