class Solution:
    def trap(self, height: List[int]) -> int:
        #get left max, right max
        n = len(height)
        rightMax= [0] * n
        leftMax = [0] * n 
        res = 0
        l_max = 0
        r_max = 0
        for i in range(1,n):
            l_max = max(l_max,height[i-1])
            leftMax[i] = l_max

        for i in range(n-2,-1,-1):
            r_max = max(r_max,height[i+1])
            rightMax[i] = r_max

        for i in range(n):
            if  min(leftMax[i],rightMax[i]) - height[i] < 0:
                res+=0
            else:
                 res+=min(leftMax[i],rightMax[i]) - height[i]
        return res

      