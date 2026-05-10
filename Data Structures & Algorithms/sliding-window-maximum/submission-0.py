

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k
        res = []
        
        # first window
        res.append(max(nums[l:r]))
        
        while r < len(nums):
            l += 1
            r += 1
            res.append(max(nums[l:r]))
        
        return res
