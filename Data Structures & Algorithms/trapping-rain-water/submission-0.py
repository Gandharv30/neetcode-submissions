class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height) 
        right = [0] * len(height)

        #populate left and right array
        last_max = 0
        for i in range(1,len(height)):
            last_max = max(last_max,height[i-1])
            left[i] = last_max
        last_max = 0
        for j in range(len(height)-2,-1,-1):
            last_max = max(last_max,height[j+1])
            right[j] = last_max
        ans = 0
        for i in range(len(height)-1):
             capacity = min(left[i],right[i]) - height[i]
             if capacity > 0:
                 ans += capacity
        return ans
        