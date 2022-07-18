class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for index in range(0,len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1
            while r > l:               
                if nums[l] + nums[r] < -nums[index]:
                    l += 1
                elif (nums[l] + nums[r] > -nums[index]):
                    r -= 1
                else:
                    res.append([nums[index],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
        return res
