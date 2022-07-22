class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0 for i in temperatures]
        
        for r in range(len(temperatures)):
            while len(stack) and stack[-1][0] < temperatures[r]:
                l = stack.pop()[1]
                res[l] = r - l
            stack.append([temperatures[r],r])
        
        return res
