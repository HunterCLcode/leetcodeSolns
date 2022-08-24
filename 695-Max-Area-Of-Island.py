class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        
        def DFS(r,c):
            if (r < 0 or
               c < 0 or
               r == ROWS or
               c == COLS or
               (r,c) in path or
               not grid[r][c]):
                return 0
            
            path.add((r,c))
            return 1 + DFS(r - 1, c) + DFS(r, c - 1) + DFS(r + 1, c) + DFS(r, c + 1)
        
        
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r,c) not in path:
                    res = max(DFS(r,c), res)
        
        return res
