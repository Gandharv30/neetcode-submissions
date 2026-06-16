"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # if there are no merges happening
        if intervals == []:
            return True

        
        intervals.sort(key = lambda x: x.start)
        ans = [intervals[0]]
        
        
        for i in range(1, len(intervals)):
            last_seen  = ans[-1]
            current_interval = intervals[i]
            if last_seen.end > current_interval.start:
               return False
            else:
                ans.append(intervals[i])
        return True


        

