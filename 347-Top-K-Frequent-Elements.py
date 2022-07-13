class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        bucketList = [[] for i in range(len(nums))]
        
        for i in hmap:
            bucketList[hmap[i]-1].append(i)

        res, index = [], len(nums) - 1
        while len(res) < k:
            for i in bucketList[index]:
                res.append(i)
            index -= 1
        return res
