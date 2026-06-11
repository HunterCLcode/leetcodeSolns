class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        flag, tank, i = 0, 0, 0

        while i != len(gas):
            tank += gas[i] - cost[i]
            i += 1
            if tank < 0:
                flag = i
                tank = 0
        
        return flag
