class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        hash_map = {}
        for val in nums:
            hash_map[val] = hash_map.get(val,0) + 1
        ans = 1
        for indx, val in enumerate(nums):
            num = val
            res = 1
            while num+1 in hash_map:
                res += 1
                num+=1
            ans = max(ans,res)



        return ans