class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        def isValid(s):
            row = [0] * 9
            for i in s:
                if i != '.':
                    row[int(i) - 1] += 1
                    if row[int(i) - 1] > 1:
                        return False
            return True      
        
        res = True
        
        for i in board:
            res &= isValid(i)
        
        for i in range(0,len(board)):
            inp = []
            for j in range(0, len(board)):
                inp.append(board[j][i])
            res &= isValid(inp)
        
        startList = [[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]
        
        for i,j in startList:
            res &= isValid([board[i][j],board[i+1][j],board[i+2][j],
            board[i][j+1],board[i+1][j+1],board[i+2][j+1],
            board[i][j+2],board[i+1][j+2],board[i+2][j+2]])
            
        return res
                
        
