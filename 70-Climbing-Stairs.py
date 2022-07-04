class Solution:
    def climbStairs(self, n: int) -> int:
        fibo = [1,1]
        for i in range(n-1):
            fibo[i%2] = sum(fibo)
        return max(fibo)