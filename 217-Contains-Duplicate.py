class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) != len(set(nums))
        hashSet = set()
        for i in range(0,len(nums)):
            before = len(hashSet)
            hashSet.add(nums[i])
            if before == len(hashSet):
                return True
        return False