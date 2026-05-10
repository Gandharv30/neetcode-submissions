class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for indx,val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], indx]
            hashmap[val] = indx