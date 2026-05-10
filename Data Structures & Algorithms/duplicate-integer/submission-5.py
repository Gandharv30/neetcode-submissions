class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for val in nums:
            hash_map[val] = hash_map.get(val,0) + 1
            if hash_map[val] > 1:
                return True
        return False