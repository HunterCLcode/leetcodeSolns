class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        pow_map = []
        power = abs(n)
        count, res = 1, x

        while count * 2 <= power:
            pow_map.append([count, res])
            count *= 2
            res *= res
        
        while pow_map:
            cur = pow_map.pop(-1)
            if power - count >= cur[0]:
                res *= cur[1]
                count += cur[0]

        return res if n > 0 else 1/res
