class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def add(d1, d2):
            d1, d2 = d1[::-1], d2[::-1]
            res, index, carry = "", 0, 0

            while index < len(d1) or index < len(d2):
                c1 = int(d1[index]) if index < len(d1) else 0
                c2 = int(d2[index]) if index < len(d2) else 0
                addition = str(c1 + c2 + carry)
                res = addition[-1] + res
                carry = int(addition[0]) if len(addition) == 2 else 0
                index += 1
            return res if not carry else str(carry) + res

        res = ""
        for n in num1:
            res += "0"
            for i in range(int(n)):
                res = add(res, num2)
            if res[0] == "0":
                res = res[1:] if len(res) > 1 else ""
        return res if res else "0"
        
