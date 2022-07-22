class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:     
        stack = []
        for p,s in sorted([[p,s] for p,s in zip(position,speed)]):
            steps = (target - p)/s
            while stack and stack[-1] <= steps:
                stack.pop()
            stack.append(steps)    
        return len(stack)
