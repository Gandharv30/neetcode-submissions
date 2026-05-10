class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        c_sum = 0 
        l = 0 
        for r in range(len(nums)):
            c_sum += nums[r]
            while c_sum >= target : 
                min_len = min(min_len,r -l + 1)
                c_sum -= nums[l]
                l+=1
            
        return 0 if min_len == float('inf') else min_len