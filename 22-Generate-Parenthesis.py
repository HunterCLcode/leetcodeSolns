class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [['(', n - 1, n]]
        res = []
        
        while len(stack):
            paren, num, endparen = stack.pop()
            if num < endparen:
                stack.append([paren + ')', num, endparen - 1])
            if num > 0:
                stack.append([paren + '(', num - 1, endparen])
            elif endparen == 0:
                res.append(paren)
        return res
