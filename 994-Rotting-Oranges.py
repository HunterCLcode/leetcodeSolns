class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS, DIRS = len(grid), len(grid[0]), [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q, fresh, time = deque(), 0, 0
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([0,r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        # BFS with time as 1st index and then row & column
        while q:
            time, cr, cc = q.popleft()
            for dr, dc in DIRS:
                r, c = cr + dr, cc + dc
                if (r < 0 or c < 0 or
                   r == ROWS or c == COLS or
                   grid[r][c] != 1):
                    continue
                grid[r][c] = 2
                q.append([time + 1,r,c])
                fresh -= 1
        return time if not fresh else -1
                    
