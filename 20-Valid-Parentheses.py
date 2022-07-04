class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenPairs = {')':'(','}':'{',']':'['}
        for c in s:
            # If closing check if corresponding top of stack is the opposite paren 
            if c in parenPairs:
                if not stack or parenPairs[c] != stack.pop():
                    return False
            # If open paren, add to stack
            else:
                stack.append(c)
        return True if not stack else False