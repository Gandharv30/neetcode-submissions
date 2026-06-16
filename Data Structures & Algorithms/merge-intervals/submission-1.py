class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            last_seen = ans[-1]
            current_interval = intervals[i]

            if last_seen[1] >= current_interval[0]:
                #merge them
                last_seen[0] = min(last_seen[0],current_interval[0])
                last_seen[1] = max(last_seen[1],current_interval[1])
            else:
                ans.append(current_interval)
        
        return ans 



