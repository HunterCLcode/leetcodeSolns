class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]
        
        while len(output) < n + 1:
            output.append(output[len(output) - 2 ** int(math.log2(len(output)))] + 1)
        return output
