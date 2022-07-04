class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = set()
        for i in range(0,len(nums)):
            numCheck = target - nums[i]
            if numCheck in hashSet:
                return [i,nums.index(numCheck)]
            hashSet.add(nums[i])