class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_ = {}
        for indx,val in enumerate(nums):
            count = 1
            if map_.get(val,None) is None:
                map_[val] = count
            else:
                map_[val] += 1
                return True
        return False
         