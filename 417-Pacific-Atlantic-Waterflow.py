class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pac, atl = set(), set()
        
        def DFS(r, c, ocean, last):
            if (r < 0 or
               c < 0 or
               r == ROWS or
               c == COLS or
               (r,c) in ocean or
               last > heights[r][c]):
                return
            ocean.add((r,c))
            DFS(r - 1, c, ocean, heights[r][c])
            DFS(r + 1, c, ocean, heights[r][c])
            DFS(r, c + 1, ocean, heights[r][c])
            DFS(r, c - 1, ocean, heights[r][c])
            return
        
        for r in range(ROWS):
            DFS(r, 0, pac, 0)
            DFS(r, COLS - 1, atl, 0)
        for c in range(COLS):
            DFS(0, c, pac, 0)
            DFS(ROWS - 1, c, atl, 0)
        
        return pac.intersection(atl)
