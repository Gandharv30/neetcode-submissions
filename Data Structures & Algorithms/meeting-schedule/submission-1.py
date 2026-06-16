class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # if there are no meetings, return True
        if intervals == []:
            return True
        
        # Sort using the object attribute
        intervals.sort(key = lambda x: x.start)
        
        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            last_seen = ans[-1]
            current_interval = intervals[i]
            
            # Check object attributes (.end and .start)
            if last_seen.end > current_interval.start:
               # An overlap was found! 
               return False
            else:
                # No overlap! Add this meeting to our list so the 
                # next loop checks against THIS meeting, not the first one.
                ans.append(current_interval)
                
        return True