class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # overlapping ? - > nums[i][1] == nums[i+1][1]
        # nums[i][1] > nums[i+1][1]
        ans = []

        i = 0 
        n =  len(intervals)
        
        # all intervals ending before 
        while (i < n) and (intervals[i][1] < newInterval[0]):
            ans.append(intervals[i])
            i+=1
        
        #merge case 
        while (i < n) and (intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i+=1
            
        ans.append(newInterval)

        # anything greater than intervals

        while i < n :
            ans.append(intervals[i])
            i+=1
        return ans

