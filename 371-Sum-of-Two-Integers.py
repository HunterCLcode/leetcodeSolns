class Solution:
    def getSum(self, a: int, b: int) -> int:

        def add(c, d):
            res, cur = 0, 1
            carry_bit = 0

            while c > 0 or d > 0:
                sum_bits = sum([c & 1, d & 1, carry_bit])
                c, d = c >> 1, d >> 1

                if sum_bits == 1 or sum_bits == 3: res += cur
                carry_bit = 1 if sum_bits >= 2 else 0

                cur *= 2
            if carry_bit: res += cur
            
            return res

        def subtract(c,d):
            res, cur = 0, 1
            carry_bit = 0

            while c > 0 or d > 0:
                sub_bits = ((c & 1) - (d & 1)) - carry_bit
                c, d = c >> 1, d >> 1

                if sub_bits == 1 or sub_bits == -1: res += cur
                carry_bit = 0 if sub_bits >= 0 else 1
                cur *= 2
                
            return res

        if a >= 0 and b >= 0: return add(a,b)
        if a < 0 and b < 0: return add(a * -1, b * -1) * -1
        negative_num, postive_num = min(a,b), max(a,b)
        if postive_num >= abs(negative_num):
            return subtract(postive_num, -1 * negative_num)
        else:
            return -1 * subtract(-1 * negative_num, postive_num)
