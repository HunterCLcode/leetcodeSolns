class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(2, numRows + 1):
            line = []
            for j in range(0,i):
                if j == 0 or j == i - 1:
                    line.append(1)
                else:
                    line.append(res[i - 2][j - 1] + res[i - 2][j])
            res.append(line)
        return res
