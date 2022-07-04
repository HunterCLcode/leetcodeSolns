class Solution:
    def isHappy(self, n: int) -> bool:
        # Floyd's Tortoise and Hare alg.!       
        s = self.getHappNum(n)
        f = self.getHappNum(s)
        if f == 1 or s == 1:
            return True
        
        while f != s:
            for i in range(2):
                f = self.getHappNum(f)
                if f == 1:
                    return True
            s = self.getHappNum(s)
        return False
    
    def getHappNum(self, num):
        nnum = 0
        for i in str(num):
            nnum += pow(int(i),2)
        return nnum
    