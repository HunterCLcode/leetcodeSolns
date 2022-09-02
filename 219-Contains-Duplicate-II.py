class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        q, hset = deque(), set()
        
        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            hset.add(nums[i])
            q.append(nums[i])
            if len(q) > k:
                hset.remove(q.popleft())
        return False
