class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res, curCol = "", columnNumber
            
        while curCol > 0:
            nextNum = int(curCol % 26)
            nextNum = 26 if not nextNum else nextNum
            res += chr(ord('A') - 1 + nextNum)
            curCol = (curCol - nextNum) / 26
        return res[::-1]
            
            
