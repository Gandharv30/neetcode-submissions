class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for indx in range(len(nums)):
            diff = target - nums[indx] 
            if diff in hash_map:
                return [hash_map[diff],indx]
            hash_map[nums[indx]] = indx 
            
        