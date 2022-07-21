class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+','-','*','/'])
        
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                n1, n2 = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(n2 + n1)
                if i == '-':
                    stack.append(n2 - n1)
                if i == '*':
                    stack.append(int(n2 * n1))
                if i == '/':
                    stack.append(int(n2 / n1))
                    
        return stack.pop()
