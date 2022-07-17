class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while r > l + 1:
            if numbers[l] + numbers[r] == target:
                return [l + 1,r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l + 1,r + 1]
