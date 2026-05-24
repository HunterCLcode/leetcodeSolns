class Solution:
    def reverse(self, x: int) -> int:
        x = int('-' + str(x)[:0:-1]) if x < 0 else int(str(x)[::-1])

        if x < -(2 ** 31) or x > (2 ** 31) - 1:
            return 0
        return x
