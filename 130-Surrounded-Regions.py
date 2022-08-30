class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def DFS(r, c):
            if (r < 0 or
               c < 0 or
               r == ROWS or
               c == COLS or 
               board[r][c] != 'O'):
                return
            board[r][c] = '0'
            DFS(r - 1, c)
            DFS(r + 1, c)
            DFS(r, c - 1)
            DFS(r, c + 1)

        for r in range(ROWS):
            DFS(r, 0)
            DFS(r, COLS - 1)
        for c in range(COLS):
            DFS(0, c)
            DFS(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == '0': board[r][c] = 'O'
        return board
