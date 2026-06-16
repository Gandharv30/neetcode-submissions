from _heapq import heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        free_rooms = []
        intervals.sort(key = lambda x: x.start)
        heapq.heappush(free_rooms,intervals[0].end)

        for interval in range(1,len(intervals)):

            if free_rooms[0] <= intervals[interval].start :
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms,intervals[interval].end)
            
        return len(free_rooms)
