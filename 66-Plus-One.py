class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        hmap = {0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
        digits[i] = hmap[digits[i]]
        
        while digits[i] == 0:                
            if i == 0:
                digits.insert(0,1)
                return digits
            i -= 1
            digits[i] = hmap[digits[i]] 
    
        return digits
            