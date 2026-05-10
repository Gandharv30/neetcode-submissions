class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            current_val = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    current_val = current_val*nums[j]
            ans[i] = current_val
        return ans