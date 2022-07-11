class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        output = ""
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b
        for i in range(len(a)-1,-1,-1):
            num = int(a[i]) + int(b[i]) + carry
            if num == 2:
                carry = 1
                output += '0'
            elif num == 3:
                carry = 1
                output += '1'
            else:
                carry = 0
                output += str(num)
        if carry == 1:
            output += '1'
        return output[::-1]
