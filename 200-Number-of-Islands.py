class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        path = set()
        def DFS(x,y):
            if (x < 0 or
               y < 0 or
               x == ROWS or
               y == COLS or
               grid[x][y] != '1' or
               (x,y) in path):
                return
            grid[x][y] = 'x'
            path.add((x,y))
            DFS(x - 1, y)
            DFS(x, y - 1)
            DFS(x + 1, y)
            DFS(x, y + 1)
            
        
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and grid[r][c] not in path:
                    res += 1
                    DFS(r,c)
        
        return res
