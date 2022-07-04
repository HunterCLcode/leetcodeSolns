class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        
        for i in range(len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        return True