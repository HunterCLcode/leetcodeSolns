class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        insert_index = 0

        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            else:
                if newInterval[0] > intervals[i][1]:
                    insert_index = i + 1
                res.append(intervals[i])

        res.insert(insert_index, newInterval)
                
        return res            
