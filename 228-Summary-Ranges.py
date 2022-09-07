class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        res, curr = [], [nums[0]]

        for i in range(1, len(nums)):
            if curr[-1] + 1 != nums[i]:
                if len(curr) == 1:
                    res.append(str(curr[0]))
                else:
                    res.append(str(curr[0]) + "->" + str(curr[-1]))
                curr = []
            curr.append(nums[i])
            
        if len(curr) == 1:
            res.append(str(curr[0]))
        else:
            res.append(str(curr[0]) + "->" + str(curr[-1]))
        return res
