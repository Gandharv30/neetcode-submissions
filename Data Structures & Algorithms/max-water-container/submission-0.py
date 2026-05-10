class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 
        l = 0
        r = len(heights) - 1
        while l < r : 
            area = (r-l)* min(heights[l],heights[r])
            if heights[l] == min(heights[l],heights[r]):
                l+=1
            else:
                r-=1
            res = max(res,area)
        return res