class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex: return [1]
        res = [1,1]
        
        for i in range(1, rowIndex):
            row = [1]
            for j in range(0, i):
                row.append(res[j] + res[j + 1])
            row.append(1)
            res = row
        return res
