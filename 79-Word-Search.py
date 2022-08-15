class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        
        def DFS(x, y, i):
            if (x < 0 or y < 0
            or x == len(board) or y == len(board[0])
            or board[x][y] != word[i] or (x,y) in path):
                return False
            if len(word) - 1 == i:
                return True
            path.add((x,y))
            res = (DFS(x - 1, y, i + 1)
            or DFS(x, y - 1, i + 1)
            or DFS(x + 1, y, i + 1)
            or DFS(x, y + 1, i + 1))
            
            path.remove((x,y))
            return res
            
        
        # Find starting letter and then call recursion
        for x in range(len(board)):
            for y in range(len(board[0])):
                if DFS(x, y, 0): return True
        return False
            
