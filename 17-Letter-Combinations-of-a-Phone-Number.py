class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        numToChars = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'],'9':['w','x','y','z']}
        
        res = []
        
        def DFS(i, s):
            if i == len(digits):
                res.append(s)
                return
            for char in numToChars[digits[i]]:
                DFS(i + 1, s + char)
            
        DFS(0, "")
        return res
