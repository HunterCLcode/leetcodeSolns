class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Takes in number and returns a 4 byte list of bits, positive only
        def toBits(num):
            output = []
            for index in range(0,32):
                bit = num % 2
                num = int(num / 2)
                output.append(bit)
                
            return output[::-1]
            
            
        # Takes in bits and returns a number, positive only
        def toNum(bits):
            output = 0
            for i in bits:
                output *= 2
                if i == 1:
                    output += 1
            return output
        
        posNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        negNum = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        for num in nums:
            bitList = toBits(abs(num))
            
            if num >= 0:
                for i in range(0,len(bitList)):
                    posNum[i] += bitList[i]
                    posNum[i] = 0 if posNum[i] == 2 else posNum[i]
            else:
                for i in range(0,len(bitList)):
                    negNum[i] += bitList[i]
                    negNum[i] = 0 if negNum[i] == 2 else negNum[i]
        
        if 1 in posNum:
            return toNum(posNum)
        elif 1 in negNum:
            return -1 * toNum(negNum)
        else:
            return 0
                
